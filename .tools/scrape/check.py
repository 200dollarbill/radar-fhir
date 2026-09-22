"""Re-fetch every source and report whether the local raw copy is still current."""
import sys
import time
from pathlib import Path

import requests

if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from tools.scrape import convert, extractors, scrape  # noqa: E402


def classify(source: dict, root: Path, fetch_fn=scrape.fetch) -> tuple[str, str]:
    local = scrape.output_path(root, source)
    if not local.exists():
        if source.get("expected_missing"):
            return "expected-missing", ""
        return "missing-local", str(local)
    meta, _ = convert.parse_document(local.read_text(encoding="utf-8"))
    try:
        html = fetch_fn(source["url"])
        body = convert.html_to_markdown(extractors.extract(source["group"], html))
    except Exception as e:
        return "failed", f"{type(e).__name__}: {e}"
    new_hash = convert.text_hash(body)
    if new_hash == meta["sha256"]:
        return "unchanged", ""
    return "changed", f"sha256 {meta['sha256'][:12]} -> {new_hash[:12]} (fetched {meta['fetched_at']})"


def main() -> int:
    sources = scrape.load_sources(scrape.SOURCES_PATH)
    counts: dict[str, int] = {}
    for i, src in enumerate(sources):
        if i:
            time.sleep(1.0)
        status, detail = classify(src, scrape.RAW_ROOT)
        counts[status] = counts.get(status, 0) + 1
        print(f"{status:<14}{src['id']}  {detail}")
    print("\n" + ", ".join(f"{k}: {v}" for k, v in sorted(counts.items())))
    return 0 if set(counts) <= {"unchanged", "expected-missing"} else 1


if __name__ == "__main__":
    sys.exit(main())
