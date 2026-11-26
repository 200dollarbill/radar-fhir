import hashlib, re, sys, pathlib, zipfile
import pytest
from lxml import etree

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from build_docx import build  # noqa: E402
from check_text import check, read  # noqa: E402

TEMPLATE = ROOT / "docs/proposal_md/proposal_revised/proposal_prata_revised.docx"
MD = ROOT / "docs/proposal_md/proposal.md"
W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
NS = {"w": W[1:-1],
      "wp": "http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing",
      "a": "http://schemas.openxmlformats.org/drawingml/2006/main",
      "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
      "w14": "http://schemas.microsoft.com/office/word/2010/wordml"}

pytestmark = pytest.mark.skipif(not TEMPLATE.exists(), reason="owner's template not present")


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


@pytest.fixture(scope="module")
def built(tmp_path_factory):
    before = sha(TEMPLATE)
    out = tmp_path_factory.mktemp("docx") / "v2.docx"
    build(TEMPLATE, MD, out)
    return {"out": out, "before": before, "zip": zipfile.ZipFile(out)}


def doc_root(b):
    return etree.fromstring(b["zip"].read("word/document.xml"))


def ptext(p):
    return "".join(t.text or "" for t in p.iter(W + "t"))


def paras_by_style(b, style):
    root = doc_root(b)
    return [ptext(p) for p in root.iter(W + "p")
            if p.find(f"{W}pPr/{W}pStyle") is not None
            and p.find(f"{W}pPr/{W}pStyle").get(W + "val") == style]


def test_owner_docx_untouched(built):
    assert sha(TEMPLATE) == built["before"]


def test_xml_parses(built):
    for name in built["zip"].namelist():
        if name.endswith(".xml") or name.endswith(".rels"):
            etree.fromstring(built["zip"].read(name))


def test_old_strings_gone(built):
    text = "\n".join(ptext(p) for p in doc_root(built).iter(W + "p"))
    for old in ("Pengembangan Profil Fast Healthcare", "Development of a Fast Healthcare",
                "Monitoring Kesehatan Berbasis RADAR", "Penelitian ini mengembangkan dan memvalidasi",
                "This research develops"):
        assert old not in text
    assert text.count("Pengembangan Sistem Pendukung Keputusan Klinis") >= 3
    assert "Development of a Clinical Decision Support System" in text


def test_headings(built):
    h2 = paras_by_style(built, "Heading2")
    assert "3.1 Pendekatan dan Alur Penelitian" in h2 and "3.12 Rencana Kerja" in h2
    assert "1.1 Latar Belakang" in h2
    assert "3.4.1 Gambaran Umum" in paras_by_style(built, "Heading3")
    h1 = paras_by_style(built, "Heading1")
    assert "DAFTAR GAMBAR" in h1 and "BAB IIIMETODOLOGI DAN PERANCANGAN SISTEM" in h1


def test_captions_styled(built):
    assert any(t.startswith("Tabel 3.4") for t in paras_by_style(built, "Heading6"))
    assert any(t.startswith("Gambar 2.2") for t in paras_by_style(built, "Heading5"))


def test_references(built):
    root = doc_root(built)
    texts = [ptext(p) for p in root.find(W + "body").iter(W + "p")]
    i = texts.index("DAFTAR PUSTAKA")
    j = texts.index("LAMPIRAN")
    refs = [t for t in texts[i + 1:j] if t.strip()]
    assert len(refs) == 41
    assert [r.split("]")[0] for r in refs] == [f"[{n}" for n in range(1, 42)]


def test_ids_unique_and_embeds_resolve(built):
    root = doc_root(built)
    pids = root.xpath("//@w14:paraId", namespaces=NS)
    assert len(pids) == len(set(pids))
    dids = root.xpath("//wp:docPr/@id", namespaces=NS)
    assert len(dids) == len(set(dids))
    rels = etree.fromstring(built["zip"].read("word/_rels/document.xml.rels"))
    targets = {r.get("Id"): r.get("Target") for r in rels}
    names = set(built["zip"].namelist())
    for rid in root.xpath("//a:blip/@r:embed", namespaces=NS):
        assert rid in targets and "word/" + targets[rid] in names


def test_update_fields(built):
    s = etree.fromstring(built["zip"].read("word/settings.xml"))
    u = s.find(W + "updateFields")
    assert u is not None and u.get(W + "val") == "true"


def test_figure_count(built):
    root = doc_root(built)
    # 6 cover images plus 9 proposal figures (Gambar 2.1, 2.2, 3.1 to 3.7)
    assert len(root.xpath("//a:blip", namespaces=NS)) == 15


def test_checker_clean(built):
    # cover pages are the ITS template's own text (course code "EB184702" has a dash)
    # words proposal.md allows with <!-- check:ok w --> stay allowed in the docx
    allowed = {w.lower() for m in re.finditer(r"<!--\s*check:ok\s+([^>]*?)\s*-->", MD.read_text())
               for w in m.group(1).split()}
    text = read(str(built["out"]))
    problems = check(text[text.index("BAB I"):])
    assert [p for p in problems if p.split("banned: ")[-1] not in allowed] == []
