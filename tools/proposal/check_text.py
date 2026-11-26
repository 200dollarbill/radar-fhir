"""Style checker for proposal text (rules from docs/proposal_guide/panduan_proposal.md).

Usage: python3 tools/proposal/check_text.py FILE [FILE...]   (.md, .txt or .docx)
Prints one line per problem and "N problem(s)"; exits 1 if any.
"""
import re
import sys
import zipfile

BANNED = ("diagnosa", "diagnosis", "prediksi", "monitoring", "pemantauan")
BANNED_STEMS = ("diagnos", "prediks", "pantau", "mantau")
NEGATORS = {"bukan", "tidak", "tanpa", "not", "no", "never"}
DASH = re.compile(r"(?<=[A-Za-z0-9])-(?=[A-Za-z0-9])|\s-\s|[–—]")
CITE = re.compile(r"\[(\d+|new)\]")
ADJ = re.compile(r"\[\d+\]\[\d+\]")
CODE = re.compile(r"`[^`]*`")
ALLOW = re.compile(r"<!--\s*check:ok\s+([^>]*?)\s*-->")
WORD = re.compile(r"[A-Za-z]+")


def _negated(words, i):
    win = words[max(0, i - 4):i]
    return any(w in NEGATORS and not (k + 1 < len(win) and win[k + 1] == "hanya")
               for k, w in enumerate(win))


RESOURCE_NAMES = {"diagnosticreport"}


def _banned(w):
    if w in RESOURCE_NAMES:
        return False
    return w in BANNED or (w.startswith(("me", "di", "ter", "pe")) and any(st in w for st in BANNED_STEMS))


def check(text):
    problems = []
    in_fence = False
    for n, line in enumerate(text.splitlines(), 1):
        if line.strip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        if line.strip().lstrip("#").strip().upper().startswith("DAFTAR PUSTAKA"):
            break
        if line.lstrip().startswith("!["):
            continue
        allowed = {w.lower() for m in ALLOW.finditer(line) for w in m.group(1).split()}
        body = CODE.sub("", ALLOW.sub("", line))
        for m in DASH.finditer(body):
            problems.append(f"line {n}: dash: {body[max(0, m.start() - 20):m.end() + 20]}")
        for m in CITE.finditer(body):
            v = m.group(1)
            if v == "new" or not 1 <= int(v) <= 41:
                problems.append(f"line {n}: citation: {m.group(0)}")
        for m in ADJ.finditer(body):
            problems.append(f"line {n}: citation: {m.group(0)} (use [a], [b])")
        words = [w.lower() for w in WORD.findall(body)]
        for i, w in enumerate(words):
            if _banned(w) and w not in allowed and not _negated(words, i):
                problems.append(f"line {n}: banned: {w}")
    return problems


def read(path):
    if path.endswith(".docx"):
        xml = zipfile.ZipFile(path).read("word/document.xml").decode()
        paras = re.findall(r"<w:p[ >].*?</w:p>", xml, re.S)
        return "\n".join("".join(re.findall(r"<w:t[^>]*>([^<]*)", p)) for p in paras)
    with open(path, encoding="utf-8") as f:
        return f.read()


def main(paths):
    total = 0
    for p in paths:
        for prob in check(read(p)):
            print(f"{p}: {prob}")
            total += 1
    print(f"{total} problem(s)")
    return 1 if total else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
