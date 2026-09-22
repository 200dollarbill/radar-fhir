"""HTML -> Markdown conversion and front-matter (de)serialisation for raw reference files."""
import hashlib
import re

import yaml
from markdownify import markdownify

_BLANKS = re.compile(r"\n{3,}")
_CF_EMAIL_PROTECTION = re.compile(r"email-protection#[0-9a-fA-F]+")


def html_to_markdown(html: str) -> str:
    md = markdownify(html, heading_style="ATX", bullets="-")
    md = _CF_EMAIL_PROTECTION.sub("email-protection", md)
    md = _BLANKS.sub("\n\n", md).strip() + "\n"
    return md


def text_hash(markdown: str) -> str:
    return hashlib.sha256(markdown.encode("utf-8")).hexdigest()


def render_document(meta: dict, body: str) -> str:
    front = yaml.safe_dump(meta, sort_keys=False, allow_unicode=True).rstrip("\n")
    return f"---\n{front}\n---\n{body}"


def parse_document(text: str) -> tuple[dict, str]:
    if not text.startswith("---\n"):
        raise ValueError("document has no front-matter")
    end = text.index("\n---\n", 4)
    meta = yaml.safe_load(text[4:end])
    body = text[end + len("\n---\n"):]
    return meta, body
