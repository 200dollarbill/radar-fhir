"""Fetch every page in sources.yaml and write docs/reference/raw/<group>/<id>.md."""
import argparse
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import requests
import yaml

if __package__ in (None, ""):  # allow `python3 tools/scrape/scrape.py`
    sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from tools.scrape import convert, extractors  # noqa: E402

HERE = Path(__file__).resolve().parent
PROJECT_ROOT = HERE.parents[1]
SOURCES_PATH = HERE / "sources.yaml"
RAW_ROOT = PROJECT_ROOT / "docs" / "reference" / "raw"
USER_AGENT = "fhir-reference-compiler/0.1 (student project)"
_BASE_KEY = {"satusehat": "satusehat_base", "fhir-r4": "fhir_r4_base", "fhir-ci": "fhir_ci_base"}
_FHIR_VERSION = {"satusehat": "R4", "fhir-r4": "R4", "fhir-ci": "R6-ci"}


def fhir_version_for(group: str) -> str:
    return _FHIR_VERSION[group]


def load_sources(path: Path) -> list[dict]:
    data = yaml.safe_load(Path(path).read_text(encoding="utf-8"))
    out, seen = [], set()
    for s in data["sources"]:
        if s["id"] in seen:
            raise ValueError(f"duplicate source id: {s['id']}")
        seen.add(s["id"])
        base = data[_BASE_KEY[s["group"]]]
        out.append({**s, "url": base + s["url"]})
    return out


def fetch(url: str, session: requests.Session | None = None, retries: int = 3) -> str:
    session = session or requests.Session()
    last_err: Exception | None = None
    for attempt in range(retries):
        try:
            r = session.get(url, headers={"User-Agent": USER_AGENT}, timeout=30)
            r.raise_for_status()
            r.encoding = r.apparent_encoding or "utf-8"
            return r.text
        except requests.RequestException as e:  # retry on any transport/HTTP error
            last_err = e
            time.sleep(2 * (attempt + 1))
    raise last_err  # type: ignore[misc]


def build_document(source: dict, html: str, fetched_at: str) -> str:
    body_html = extractors.extract(source["group"], html)
    body = convert.html_to_markdown(body_html)
    meta = {
        "id": source["id"],
        "title": source["title"],
        "source_url": source["url"],
        "group": source["group"],
        "fhir_version": fhir_version_for(source["group"]),
        "fetched_at": fetched_at,
        "sha256": convert.text_hash(body),
    }
    return convert.render_document(meta, body)


def output_path(root: Path, source: dict) -> Path:
    return Path(root) / source["group"] / f"{source['id']}.md"


def run(sources: list[dict], root: Path, fetch_fn=fetch, sleep_fn=time.sleep) -> list[tuple[str, str]]:
    failures: list[tuple[str, str]] = []
    for i, src in enumerate(sources):
        if i:
            sleep_fn(1.0)
        fetched_at = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        try:
            html = fetch_fn(src["url"])
            text = build_document(src, html, fetched_at)
        except Exception as e:  # any per-source failure must not abort the batch
            failures.append((src["id"], str(e)))
            print(f"FAIL  {src['id']}: {e}")
            continue
        path = output_path(root, src)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
        print(f"ok    {src['id']} -> {path.relative_to(PROJECT_ROOT) if path.is_relative_to(PROJECT_ROOT) else path}")
    return failures


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--only", nargs="*", help="source ids to fetch (default: all)")
    args = ap.parse_args(argv)
    sources = load_sources(SOURCES_PATH)
    if args.only:
        sources = [s for s in sources if s["id"] in set(args.only)]
    failures = run(sources, RAW_ROOT)
    print(f"\n{len(sources) - len(failures)} written, {len(failures)} failed")
    for sid, msg in failures:
        print(f"  - {sid}: {msg}")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
