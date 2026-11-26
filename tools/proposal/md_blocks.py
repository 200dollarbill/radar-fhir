"""Parse proposal.md into blocks for the template docx builder.

Conventions are pinned in docs/design/plans/2026-11-26-proposal-merge-and-bab3.md.
"""
from __future__ import annotations

import pathlib
import re
from dataclasses import dataclass, field

IMG = re.compile(r"^!\[(.*?)\]\((.*?)\)\s*$")
REF = re.compile(r"^\[\d+\] ")
COMMENT = re.compile(r"\s*<!--.*?-->")
BOLD = re.compile(r"\*\*(.+?)\*\*")


@dataclass
class Block:
    kind: str                      # h1 h2 h3 p img table listing formula
    text: str = ""
    runs: list = field(default_factory=list)
    path: pathlib.Path | None = None
    rows: list = field(default_factory=list)
    lines: list = field(default_factory=list)


@dataclass
class Doc:
    title_id: str = ""
    title_en: str = ""
    abstrak: list = field(default_factory=list)
    kata_kunci: str = ""
    abstract: list = field(default_factory=list)
    keywords: str = ""
    body: list = field(default_factory=list)
    references: list = field(default_factory=list)


def clean(text: str) -> str:
    return COMMENT.sub("", text).replace("`", "").strip()


def runs(text: str) -> list:
    out, pos = [], 0
    for m in BOLD.finditer(text):
        if m.start() > pos:
            out.append((text[pos:m.start()], False))
        out.append((m.group(1), True))
        pos = m.end()
    if pos < len(text):
        out.append((text[pos:], False))
    return out


def _paragraphs(lines):
    """Split lines into groups separated by blank lines; fenced blocks stay whole."""
    groups, cur, fence = [], [], False
    for line in lines:
        if line.strip().startswith("```"):
            if fence:
                cur.append(line)
                groups.append(cur)
                cur, fence = [], False
                continue
            if cur:
                groups.append(cur)
            cur, fence = [line], True
            continue
        if fence:
            cur.append(line)
        elif not line.strip():
            if cur:
                groups.append(cur)
            cur = []
        else:
            cur.append(line)
    if cur:
        groups.append(cur)
    return groups


def _row(line):
    return [c.strip() for c in line.strip().strip("|").split("|")]


def _body(lines, base):
    blocks = []
    for g in _paragraphs(lines):
        first = g[0].strip()
        if first.startswith("```"):
            info = first[3:].strip()
            inner = [l.rstrip("\n") for l in g[1:-1]]
            blocks.append(Block("formula" if info == "rumus" else "listing", lines=inner))
            continue
        if first == "---":
            continue
        if first.startswith("#"):
            level = len(first) - len(first.lstrip("#"))
            kind = {2: "h1", 3: "h2", 4: "h3"}[level]
            blocks.append(Block(kind, text=clean(first.lstrip("#"))))
            continue
        m = IMG.match(first)
        if m:
            path = (base / m.group(2)).resolve()
            if not path.exists():
                raise FileNotFoundError(f"figure not found: {m.group(2)} ({path})")
            blocks.append(Block("img", text=clean(m.group(1)), path=path))
            continue
        if first.startswith("|"):
            rows = [_row(l) for l in g if not re.fullmatch(r"\|?[\s:|-]+\|?", l.strip())]
            caption = ""
            if blocks and blocks[-1].kind == "p" and blocks[-1].text.startswith("Tabel "):
                caption = blocks.pop().text
            blocks.append(Block("table", text=caption, rows=[[clean(c) for c in r] for r in rows]))
            continue
        text = clean(" ".join(l.strip() for l in g))
        if not text:
            continue
        if text.startswith("Listing ") and blocks and blocks[-1].kind == "listing":
            blocks[-1].text = text
            continue
        blocks.append(Block("p", text=BOLD.sub(r"\1", text), runs=runs(text)))
    return blocks


def parse(text: str, base: pathlib.Path) -> Doc:
    doc = Doc()
    lines = text.splitlines()
    sections, name = {}, None
    for i, line in enumerate(lines):
        if line.startswith("## "):
            name = line[3:].strip()
            sections.setdefault(name, i)
    order = sorted(sections.items(), key=lambda kv: kv[1])

    def span(title):
        if title not in sections:
            return []
        start = sections[title]
        nxt = [i for _, i in order if i > start]
        return lines[start + 1:(nxt[0] if nxt else len(lines))]

    def first_text(title):
        return next((l.strip() for l in span(title) if l.strip()), "")

    doc.title_id = first_text("Judul:")
    doc.title_en = first_text("Judul (Inggris):")
    for title, attr, kw, prefix in (("ABSTRAK", "abstrak", "kata_kunci", "Kata kunci:"),
                                    ("ABSTRACT", "abstract", "keywords", "Keywords:")):
        paras = [" ".join(g) for g in _paragraphs(span(title)) if g[0].strip() != "---"]
        setattr(doc, kw, next((p for p in paras if p.startswith(prefix)), ""))
        setattr(doc, attr, [clean(p) for p in paras if not p.startswith(prefix)])

    start = next(i for t, i in order if t.startswith("BAB I "))
    end = sections["DAFTAR PUSTAKA"]
    doc.body = _body(lines[start:end], base)
    for line in lines[end + 1:]:
        if REF.match(line):
            doc.references.append(line.strip())
        elif line.strip() and doc.references:
            break
    return doc
