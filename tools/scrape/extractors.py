"""Per-site main-content extraction. Returns inner HTML of the content element."""
from bs4 import BeautifulSoup


class PageMissing(Exception):
    """The page exists over HTTP but has no real content (404-as-200, redirect notice)."""


_STRIP_TAGS = ("script", "style", "nav", "aside", "footer", "header", "iframe", "svg")


def _strip(el):
    for tag in el.find_all(_STRIP_TAGS):
        tag.decompose()
    return el


def _extract_satusehat(html: str) -> str:
    soup = BeautifulSoup(html, "html.parser")
    title = soup.title.get_text(strip=True) if soup.title else ""
    if "Redirect Notice" in title:
        raise PageMissing("SATUSEHAT redirect notice (page does not exist)")
    article = soup.select_one("article.doc")
    if article is None:
        raise PageMissing("no <article class='doc'> found")
    return _strip(article).decode_contents()


def _extract_hl7(html: str) -> str:
    soup = BeautifulSoup(html, "html.parser")
    content = soup.select_one("div#segment-content")
    if content is None:
        raise PageMissing("no <div id='segment-content'> found")
    return _strip(content).decode_contents()


_EXTRACTORS = {
    "satusehat": _extract_satusehat,
    "fhir-r4": _extract_hl7,
    "fhir-ci": _extract_hl7,
}


def extract(group: str, html: str) -> str:
    try:
        fn = _EXTRACTORS[group]
    except KeyError:
        raise ValueError(f"unknown group: {group!r}") from None
    return fn(html)
