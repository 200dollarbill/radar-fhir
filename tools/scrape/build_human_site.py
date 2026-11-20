"""Render docs/reference/human/*.md into one self-contained HTML page for publishing."""
import html
import re
import sys
from pathlib import Path

import markdown

_MERMAID = re.compile(r"```mermaid\n(.*?)```", re.S)
_PLACEHOLDER = "MERMAIDPLACEHOLDER{}"
_STYLE = """
:root{--bg:#f5f7f8;--fg:#16211f;--muted:#5c6b68;--line:#d5dcda;--accent:#0f7a6e;--code-bg:#e9eeed}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]){--bg:#121817;--fg:#e6ecea;--muted:#97a5a1;--line:#2a3533;--accent:#4fc3b0;--code-bg:#1b2422}}
:root[data-theme="dark"]{--bg:#121817;--fg:#e6ecea;--muted:#97a5a1;--line:#2a3533;--accent:#4fc3b0;--code-bg:#1b2422}
body{background:var(--bg);color:var(--fg);font:16px/1.6 "IBM Plex Sans",system-ui,sans-serif;margin:0;padding-block:32px;padding-inline:16px}
h1,h2,h3,h4{font-family:"IBM Plex Serif",Georgia,serif;font-weight:600;line-height:1.2;text-wrap:balance;margin:1.6em 0 .5em}
h1{font-size:1.9rem;margin-top:0}h2{font-size:1.4rem}h3{font-size:1.15rem}
.wrap{display:flex;gap:40px;max-width:1120px;margin:auto}
nav{flex:0 0 230px;position:sticky;top:16px;align-self:flex-start;font-size:.85rem;border-left:2px solid var(--line);padding-left:12px}
nav a{display:block;color:var(--muted);text-decoration:none;padding:4px 0}
nav a:hover,nav a:focus-visible{color:var(--accent);outline:none}
nav a:focus-visible{text-decoration:underline}
main{flex:1;min-width:0;max-width:72ch}
main a{color:var(--accent)}
section{border-top:1px solid var(--line);padding-top:28px;margin-top:28px}
section:first-child{border-top:0;padding-top:0;margin-top:0}
table{border-collapse:collapse;display:block;overflow-x:auto;max-width:100%;font-size:.9rem;font-variant-numeric:tabular-nums}
td,th{border:1px solid var(--line);padding:5px 9px;text-align:left;vertical-align:top}
th{font-weight:600;color:var(--muted);font-size:.78rem;letter-spacing:.04em;text-transform:uppercase}
pre{overflow-x:auto;background:var(--code-bg);padding:12px 14px;border-radius:3px}
pre.mermaid{background:transparent;padding:0}
code{font-family:"IBM Plex Mono",ui-monospace,monospace;font-size:.88em}
blockquote{border-left:3px solid var(--accent);margin:1em 0;padding:.2em 1em;color:var(--muted)}
@media (max-width:760px){.wrap{flex-direction:column;gap:24px}nav{position:static;flex:none}}
@media (prefers-reduced-motion:no-preference){html{scroll-behavior:smooth}}
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
    return (f"<title>SATUSEHAT FHIR Reference</title>"
            f'<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;600&family=IBM+Plex+Serif:wght@600&family=IBM+Plex+Mono&display=swap">'
            f"<style>{_STYLE}</style>"
            f'<div class="wrap"><nav>{"".join(nav)}</nav><main>{"".join(parts)}</main></div>')


if __name__ == "__main__":
    human = Path(__file__).resolve().parents[2] / "docs" / "reference" / "human"
    out = Path(sys.argv[1])
    out.write_text(build(human), encoding="utf-8")
    print(f"wrote {out} ({out.stat().st_size} bytes)")
