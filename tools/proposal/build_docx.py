"""Build the proposal docx from the owner's ITS template and proposal.md.

Usage: python3 tools/proposal/build_docx.py TEMPLATE.docx proposal.md OUT.docx

Keeps covers, styles, footers and TOC fields of the template; replaces titles, abstracts,
Bab I to III and the reference list. The template file is only read.
"""
from __future__ import annotations

import copy
import pathlib
import re
import sys
import zipfile

from lxml import etree
from PIL import Image

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from md_blocks import parse  # noqa: E402

WNS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
W = "{%s}" % WNS
R = "{http://schemas.openxmlformats.org/officeDocument/2006/relationships}"
W14 = "{http://schemas.microsoft.com/office/word/2010/wordml}"
REL_IMAGE = "http://schemas.openxmlformats.org/officeDocument/2006/relationships/image"
OLD_TITLES = ("Pengembangan Profil Fast Healthcare", "Development of a Fast Healthcare")
MAX_W, MAX_H = 5040000, 7920000          # 14 cm by 22 cm in EMU
SETTINGS_AFTER = ("hdrShapeDefaults", "footnotePr", "endnotePr", "compat", "docVars",
                  "rsids", "mathPr", "attachedSchema", "themeFontLang", "clrSchemeMapping",
                  "doNotIncludeSubdocsInStats", "doNotAutoCompressPictures", "forceUpgrade",
                  "captions", "readModeInkLockDown", "smartTagType", "schemaLibrary",
                  "shapeDefaults", "doNotEmbedSmartTags", "decimalSymbol", "listSeparator")
LISTING_STYLE = (
    f'<w:style xmlns:w="{WNS}" w:type="paragraph" w:customStyle="1" w:styleId="Listing">'
    '<w:name w:val="Listing"/><w:basedOn w:val="Normal"/><w:pPr>'
    '<w:spacing w:before="0" w:after="0" w:line="240" w:lineRule="auto"/>'
    '<w:ind w:firstLine="0"/><w:jc w:val="left"/></w:pPr><w:rPr>'
    '<w:rFonts w:ascii="Courier New" w:hAnsi="Courier New" w:cs="Courier New"/>'
    '<w:sz w:val="18"/><w:szCs w:val="18"/></w:rPr></w:style>')


PPR_ORDER = ["pStyle", "keepNext", "keepLines", "pageBreakBefore", "framePr", "widowControl",
             "numPr", "suppressLineNumbers", "pBdr", "shd", "tabs", "suppressAutoHyphens",
             "kinsoku", "wordWrap", "overflowPunct", "topLinePunct", "autoSpaceDE",
             "autoSpaceDN", "bidi", "adjustRightInd", "snapToGrid", "spacing", "ind",
             "contextualSpacing", "mirrorIndents", "suppressOverlap", "jc", "textDirection",
             "textAlignment", "textboxTightWrap", "outlineLvl", "divId", "cnfStyle", "rPr",
             "sectPr", "pPrChange"]
RPR_ORDER = ["rStyle", "rFonts", "b", "bCs", "i", "iCs", "caps", "smallCaps", "strike",
             "dstrike", "outline", "shadow", "emboss", "imprint", "noProof", "snapToGrid",
             "vanish", "webHidden", "color", "spacing", "w", "kern", "position", "sz", "szCs",
             "highlight", "u", "effect", "bdr", "shd", "fitText", "vertAlign", "rtl", "cs",
             "em", "lang", "eastAsianLayout", "specVanish", "oMath"]


def order(e, names):
    rank = {n: i for i, n in enumerate(names)}
    kids = sorted(list(e), key=lambda c: rank.get(etree.QName(c).localname, len(names)))
    for c in kids:
        e.remove(c)
    for c in kids:
        e.append(c)
    return e


def el(tag, attrs=None, children=()):
    e = etree.Element(W + tag)
    for k, v in (attrs or {}).items():
        e.set(W + k, str(v))
    for c in children:
        e.append(c)
    return e


def text(p):
    return "".join(t.text or "" for t in p.iter(W + "t"))


def run(t, bold=False, italic=False, rpr=None, unbold=False):
    """A text run. rpr (template formatting) is kept as is unless bold or unbold is asked."""
    r = el("r")
    rp = copy.deepcopy(rpr) if rpr is not None else el("rPr")
    if bold or unbold:
        for tag in ("b", "bCs"):
            for x in rp.findall(W + tag):
                rp.remove(x)
        val = "1" if bold else "0"
        rp.append(el("b", {"val": val}))
        rp.append(el("bCs", {"val": val}))
    if italic:
        rp.append(el("i", {"val": "1"}))
    if len(rp):
        r.append(order(rp, RPR_ORDER))
    tt = el("t")
    tt.text = t
    tt.set("{http://www.w3.org/XML/1998/namespace}space", "preserve")
    r.append(tt)
    return r


def para(runs_, style=None, center=False, no_indent=False, page_break=False, keep_next=False,
         extra_ppr=()):
    ppr = el("pPr")
    if style:
        ppr.append(el("pStyle", {"val": style}))
    if keep_next:
        ppr.append(el("keepNext", {"val": "1"}))
    if page_break:
        ppr.append(el("pageBreakBefore", {"val": "1"}))
    for x in extra_ppr:
        ppr.append(x)
    if no_indent or center:
        ppr.append(el("ind", {"left": 0, "firstLine": 0}))
    if center:
        ppr.append(el("jc", {"val": "center"}))
    seen, keep = set(), []
    for c in ppr:                       # first occurrence of a tag wins
        n = etree.QName(c).localname
        if n not in seen:
            seen.add(n)
            keep.append(c)
    for c in list(ppr):
        if c not in keep:
            ppr.remove(c)
    p = el("p", children=[order(ppr, PPR_ORDER)])
    for r in runs_:
        p.append(r)
    return p


def caption(t, style):
    m = re.match(r"((?:Gambar|Tabel|Listing) [\d.]+)(.*)", t)
    head, rest = (m.group(1), m.group(2)) if m else (t, "")
    return para([run(head, bold=True), run(rest, unbold=True)], style=style, center=True,
                keep_next=style == "Heading6")


class Builder:
    def __init__(self, zin: zipfile.ZipFile):
        self.parts = {n: zin.read(n) for n in zin.namelist()}
        self.doc = etree.fromstring(self.parts["word/document.xml"])
        self.body = self.doc.find(W + "body")
        self.rels = etree.fromstring(self.parts["word/_rels/document.xml.rels"])
        nums = [int(m) for r in self.rels for m in re.findall(r"\d+", r.get("Id"))]
        self.next_rid = max(nums) + 1
        ids = [int(x) for x in self.doc.xpath(
            "//wp:docPr/@id",
            namespaces={"wp": "http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing"})]
        self.next_docpr = max(ids) + 1
        self.n_media = 0

    # ---------- front matter ----------
    def set_text(self, p, runs_):
        first = p.find(W + "r")
        rpr = first.find(W + "rPr") if first is not None else None
        for child in list(p):
            if child.tag != W + "pPr":
                p.remove(child)
        for t, b in runs_:
            p.append(run(t, bold=b, rpr=rpr))

    def front(self, d):
        for p in list(self.body.iter(W + "p")):
            t = text(p)
            if t.startswith(OLD_TITLES[0]):
                self.set_text(p, [(d.title_id, False)])
            elif t.startswith(OLD_TITLES[1]):
                self.set_text(p, [(d.title_en, False)])
            elif t.startswith("Penelitian ini mengembangkan"):
                self.abstract(p, d.abstrak)
            elif t.startswith("This research develops"):
                self.abstract(p, d.abstract)
            elif t.startswith("Kata kunci:"):
                self.set_text(p, [("Kata kunci:", True), (d.kata_kunci[len("Kata kunci:"):], False)])
            elif t.startswith("Keywords:"):
                self.set_text(p, [("Keywords:", True), (d.keywords[len("Keywords:"):], False)])

    def abstract(self, p, paras):
        self.set_text(p, [(paras[0], False)])
        prev = p
        for extra in paras[1:]:
            q = copy.deepcopy(p)
            self.set_text(q, [(extra, False)])
            prev.addnext(q)
            prev = q

    # ---------- body ----------
    def top_heading(self, pred):
        for c in self.body:
            s = c.find(f"{W}pPr/{W}pStyle")
            if c.tag == W + "p" and s is not None and s.get(W + "val") == "Heading1" and pred(text(c)):
                return c
        raise ValueError("heading not found")

    def image(self, path):
        self.n_media += 1
        ext = path.suffix.lower().lstrip(".")
        name = f"media/proposal_fig{self.n_media}.{ext}"
        self.parts["word/" + name] = path.read_bytes()
        rid = f"rId{self.next_rid}"
        self.next_rid += 1
        rel = etree.SubElement(self.rels, "{http://schemas.openxmlformats.org/package/2006/relationships}Relationship")
        rel.set("Id", rid)
        rel.set("Type", REL_IMAGE)
        rel.set("Target", name)
        with Image.open(path) as im:
            iw, ih = im.size
        cx = MAX_W
        cy = int(cx * ih / iw)
        if cy > MAX_H:
            cy, cx = MAX_H, int(MAX_H * iw / ih)
        did = self.next_docpr
        self.next_docpr += 1
        xml = f'''<w:r xmlns:w="{WNS}"><w:drawing><wp:inline distT="0" distB="0" distL="0" distR="0"
 xmlns:wp="http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing">
<wp:extent cx="{cx}" cy="{cy}"/><wp:docPr id="{did}" name="Gambar {did}"/>
<wp:cNvGraphicFramePr><a:graphicFrameLocks xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" noChangeAspect="1"/></wp:cNvGraphicFramePr>
<a:graphic xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main">
<a:graphicData uri="http://schemas.openxmlformats.org/drawingml/2006/picture">
<pic:pic xmlns:pic="http://schemas.openxmlformats.org/drawingml/2006/picture">
<pic:nvPicPr><pic:cNvPr id="{did}" name="{path.name}"/><pic:cNvPicPr/></pic:nvPicPr>
<pic:blipFill><a:blip xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" r:embed="{rid}"/><a:stretch><a:fillRect/></a:stretch></pic:blipFill>
<pic:spPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="{cx}" cy="{cy}"/></a:xfrm><a:prstGeom prst="rect"><a:avLst/></a:prstGeom></pic:spPr>
</pic:pic></a:graphicData></a:graphic></wp:inline></w:drawing></w:r>'''
        return etree.fromstring(xml)

    def table(self, rows):
        border = lambda tag: el(tag, {"val": "single", "sz": 4, "space": 0, "color": "000000"})
        tblpr = el("tblPr", children=[
            el("tblW", {"w": 5000, "type": "pct"}), el("jc", {"val": "center"}),
            el("tblBorders", children=[border(t) for t in
                                       ("top", "left", "bottom", "right", "insideH", "insideV")]),
            el("tblLayout", {"type": "autofit"}),
            el("tblCellMar", children=[el("left", {"w": 80, "type": "dxa"}),
                                       el("right", {"w": 80, "type": "dxa"})])])
        ncol = max(len(r) for r in rows)
        grid = el("tblGrid", children=[el("gridCol", {"w": 9000 // ncol}) for _ in range(ncol)])
        tbl = el("tbl", children=[tblpr, grid])
        for i, r in enumerate(rows):
            trpr = el("trPr", children=[el("tblHeader")]) if i == 0 else el("trPr", children=[el("cantSplit")])
            tr = el("tr", children=[trpr])
            for c in r + [""] * (ncol - len(r)):
                rp = el("rPr", children=[el("sz", {"val": 20}), el("szCs", {"val": 20})])
                p = para([run(c, bold=i == 0, rpr=rp)], no_indent=True,
                         extra_ppr=[el("spacing", {"before": 0, "after": 0, "line": 240, "lineRule": "auto"}),
                                    el("jc", {"val": "left"})])
                tr.append(el("tc", children=[el("tcPr", children=[el("tcW", {"w": 0, "type": "auto"})]), p]))
            tbl.append(tr)
        return tbl

    def blocks(self, body):
        out, first_h1 = [], True
        for b in body:
            if b.kind == "h1":
                m = re.match(r"(BAB [IVX]+) (.*)", b.text)
                p = para([], style="Heading1", no_indent=True, page_break=not first_h1)
                r = run(m.group(1))
                r.append(el("br"))
                t = el("t")
                t.text = m.group(2)
                r.append(t)
                p.append(r)
                out.append(p)
                first_h1 = False
            elif b.kind in ("h2", "h3"):
                out.append(para([run(b.text)], style="Heading2" if b.kind == "h2" else "Heading3"))
            elif b.kind == "p":
                out.append(para([run(t, bold=bb) for t, bb in b.runs]))
            elif b.kind == "img":
                out.append(para([self.image(b.path)], center=True, keep_next=True))
                out.append(caption(b.text, "Heading5"))
            elif b.kind == "table":
                if b.text:
                    out.append(caption(b.text, "Heading6"))
                out.append(self.table(b.rows))
                out.append(para([], no_indent=True))
            elif b.kind == "listing":
                for line in b.lines:
                    out.append(para([run(line)], style="Listing"))
                if b.text:
                    out.append(caption(b.text, None))
            elif b.kind == "formula":
                for line in b.lines:
                    out.append(para([run(line)], center=True))
        return out

    def replace_body(self, d):
        bab1 = self.top_heading(lambda t: t.startswith("BAB I") and "PENDAHULUAN" in t)
        pustaka = self.top_heading(lambda t: t == "DAFTAR PUSTAKA")
        lampiran = self.top_heading(lambda t: t == "LAMPIRAN")
        kids = list(self.body)
        for c in kids[kids.index(bab1):kids.index(pustaka)] + kids[kids.index(pustaka) + 1:kids.index(lampiran)]:
            self.body.remove(c)
        for p in self.blocks(d.body):
            pustaka.addprevious(p)
        prev = pustaka
        for ref in d.references:
            q = para([run(ref)], extra_ppr=[el("ind", {"left": 567, "hanging": 567}),
                                           el("jc", {"val": "left"})])
            prev.addnext(q)
            prev = q
        for h in (pustaka, lampiran):
            ppr = h.find(W + "pPr")
            ppr.append(el("pageBreakBefore", {"val": "1"}))
            order(ppr, PPR_ORDER)

    def list_of_figures(self):
        tabel = self.top_heading(lambda t: t == "DAFTAR TABEL")
        sdt = tabel.getnext()
        while sdt is not None and sdt.tag != W + "sdt":
            sdt = sdt.getnext()
        if sdt is None:
            raise ValueError("DAFTAR TABEL field not found")
        head = copy.deepcopy(tabel)
        for x in list(head.iter(W + "bookmarkStart", W + "bookmarkEnd")):
            x.getparent().remove(x)
        self.set_text(head, [("DAFTAR GAMBAR", False)])
        order(head.find(W + "pPr"), PPR_ORDER).append(el("pageBreakBefore", {"val": "1"}))
        order(head.find(W + "pPr"), PPR_ORDER)
        toc = copy.deepcopy(sdt)
        toc.find(f"{W}sdtPr/{W}id").set(W + "val", "-1017473979")
        self.reset_toc(toc, ' TOC \\h \\u \\z \\t "Heading 5,1," ')
        sdt.addnext(head)
        head.addnext(toc)

    def reset_toc(self, sdt, instr_text=None):
        """Drop cached entries (they hold the old headings); Word rebuilds on open."""
        content = sdt.find(W + "sdtContent")
        paras = content.findall(W + "p")
        first = paras[0]
        if instr_text is None:
            instr_text = "".join(t.text or "" for t in sdt.iter(W + "instrText"))
        for p in paras[1:]:
            content.remove(p)
        ppr = first.find(W + "pPr")
        for c in list(first):
            if c is not ppr:
                first.remove(c)
        instr = el("instrText")
        instr.text = instr_text
        instr.set("{http://www.w3.org/XML/1998/namespace}space", "preserve")
        first.extend([el("r", children=[el("fldChar", {"fldCharType": "begin", "dirty": "true"})]),
                      el("r", children=[instr]),
                      el("r", children=[el("fldChar", {"fldCharType": "separate"})]),
                      run("Perbarui daftar ini di Word (klik kanan, Update Field)."),
                      el("r", children=[el("fldChar", {"fldCharType": "end"})])])

    def reset_all_tocs(self):
        for sdt in list(self.body.iter(W + "sdt")):
            if any("TOC" in (t.text or "") for t in sdt.iter(W + "instrText")):
                self.reset_toc(sdt)

    def renumber_docpr(self):
        wp = "{http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing}"
        for i, d in enumerate(self.doc.iter(wp + "docPr"), start=1):
            d.set("id", str(i))

    # ---------- other parts ----------
    def cleanup(self):
        for tag in ("commentRangeStart", "commentRangeEnd", "commentReference"):
            for x in list(self.doc.iter(W + tag)):
                parent = x.getparent()
                parent.remove(x)
                if parent.tag == W + "r" and not len([c for c in parent if c.tag != W + "rPr"]):
                    parent.getparent().remove(parent)
        seen = set()
        for x in self.doc.iter():
            for a in (W14 + "paraId", W14 + "textId"):
                v = x.get(a)
                if v is None:
                    continue
                if a == W14 + "paraId" and v in seen:
                    del x.attrib[a]
                    x.attrib.pop(W14 + "textId", None)
                seen.add(v)
        for name in ("word/comments.xml", "word/commentsExtended.xml",
                     "word/commentsIds.xml", "word/commentsExtensible.xml"):
            if name in self.parts:
                root = etree.fromstring(self.parts[name])
                for c in list(root):
                    root.remove(c)
                self.parts[name] = etree.tostring(root, xml_declaration=True,
                                                  encoding="UTF-8", standalone=True)

    def settings(self):
        s = etree.fromstring(self.parts["word/settings.xml"])
        for x in s.findall(W + "updateFields"):
            s.remove(x)
        u = el("updateFields", {"val": "true"})
        after = next((c for c in s if etree.QName(c).localname in SETTINGS_AFTER), None)
        if after is not None:
            after.addprevious(u)
        else:
            s.append(u)
        self.parts["word/settings.xml"] = etree.tostring(s, xml_declaration=True,
                                                         encoding="UTF-8", standalone=True)

    def styles(self):
        s = etree.fromstring(self.parts["word/styles.xml"])
        if s.find(f"{W}style[@{W}styleId='Listing']") is None:
            s.append(etree.fromstring(LISTING_STYLE))
        self.parts["word/styles.xml"] = etree.tostring(s, xml_declaration=True,
                                                       encoding="UTF-8", standalone=True)

    def write(self, out):
        self.parts["word/document.xml"] = etree.tostring(self.doc, xml_declaration=True,
                                                         encoding="UTF-8", standalone=True)
        self.parts["word/_rels/document.xml.rels"] = etree.tostring(
            self.rels, xml_declaration=True, encoding="UTF-8", standalone=True)
        with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
            for name in ["[Content_Types].xml"] + [n for n in self.parts if n != "[Content_Types].xml"]:
                z.writestr(name, self.parts[name])


def build(template: pathlib.Path, md: pathlib.Path, out: pathlib.Path) -> None:
    template, md, out = map(pathlib.Path, (template, md, out))
    if out.resolve() == template.resolve():
        raise ValueError("refusing to overwrite the template")
    d = parse(md.read_text(encoding="utf-8"), md.parent)
    with zipfile.ZipFile(template) as zin:
        b = Builder(zin)
    b.front(d)
    b.replace_body(d)
    b.reset_all_tocs()
    b.list_of_figures()
    b.renumber_docpr()
    b.cleanup()
    b.settings()
    b.styles()
    b.write(out)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit(__doc__)
    build(*map(pathlib.Path, sys.argv[1:]))
    print(f"wrote {sys.argv[3]}")
