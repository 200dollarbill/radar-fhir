"""Render docs/reference/human/*.md into one self-contained HTML page for publishing."""
import html
import re
import sys
from pathlib import Path

import markdown

_MERMAID = re.compile(r"```mermaid\n(.*?)```", re.S)
_PLACEHOLDER = "MERMAIDPLACEHOLDER{}"
_STYLE = """
:root{--bg:#fafaf8;--fg:#1a1a1a;--muted:#666;--line:#ddd;--accent:#0b5}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]){--bg:#141414;--fg:#eee;--muted:#aaa;--line:#333}}
:root[data-theme="dark"]{--bg:#141414;--fg:#eee;--muted:#aaa;--line:#333}
body{background:var(--bg);color:var(--fg);font:16px/1.55 system-ui,sans-serif;margin:0;padding-block:24px;padding-inline:16px}
.wrap{display:flex;gap:32px;max-width:1100px;margin:auto}
nav{flex:0 0 220px;position:sticky;top:16px;align-self:flex-start;font-size:14px}
nav a{display:block;color:var(--fg);text-decoration:none;padding:4px 0}
main{flex:1;min-width:0}
section{border-top:1px solid var(--line);padding-top:24px;margin-top:24px}
table{border-collapse:collapse;display:block;overflow-x:auto;max-width:100%}
td,th{border:1px solid var(--line);padding:4px 8px;text-align:left;vertical-align:top}
pre{overflow-x:auto;background:rgba(127,127,127,.12);padding:12px}
code{font-size:.92em}
@media (max-width:760px){.wrap{flex-direction:column}nav{position:static;flex:none}}
"""


def _order(human_dir: Path) -> list[Path]:
    """README.md first, then the rest by filename, with validity-review.md last."""
    files = sorted(
        p
        for p in human_dir.glob("*.md")
        if p.name not in ("README.md", "validity-review.md")
    )
    ordered = [human_dir / "README.md"] + files
    review = human_dir / "validity-review.md"
    if review.exists():
        ordered.append(review)
    return ordered


def build(human_dir: Path) -> str:
    md = markdown.Markdown(extensions=["tables", "fenced_code", "toc"])
    parts, nav = [], []
    for f in _order(human_dir):
        text = f.read_text(encoding="utf-8")

        mermaid_blocks: list[str] = []

        def _stash(m: "re.Match[str]") -> str:
            mermaid_blocks.append(m.group(1))
            return f"\n\n{_PLACEHOLDER.format(len(mermaid_blocks) - 1)}\n\n"

        text = _MERMAID.sub(_stash, text)
        page_html = md.reset().convert(text)

        for i, block in enumerate(mermaid_blocks):
            token = _PLACEHOLDER.format(i)
            replacement = f'<pre class="mermaid">{html.escape(block)}</pre>'
            # Markdown wraps a lone-line token in a <p>; strip that wrapper too.
            for variant in (f"<p>{token}</p>", token):
                if variant in page_html:
                    page_html = page_html.replace(variant, replacement)
                    break

        title = next((l[2:] for l in text.splitlines() if l.startswith("# ")), f.stem)
        sid = f.stem
        nav.append(f'<a href="#{sid}">{title}</a>')
        parts.append(f'<section id="{sid}">{page_html}</section>')
    return (f"<title>SATUSEHAT FHIR Reference</title><style>{_STYLE}</style>"
            f'<div class="wrap"><nav>{"".join(nav)}</nav><main>{"".join(parts)}</main></div>')


if __name__ == "__main__":
    human = Path(__file__).resolve().parents[2] / "docs" / "reference" / "human"
    out = Path(sys.argv[1])
    out.write_text(build(human), encoding="utf-8")
    print(f"wrote {out} ({out.stat().st_size} bytes)")
