"""Style checker for proposal text (rules from docs/proposal_guide/panduan_proposal.md).

Usage: python3 tools/proposal/check_text.py FILE [FILE...]   (.md, .txt or .docx)
Prints one line per problem and "N problem(s)"; exits 1 if any.
"""
import re
import sys
import zipfile

BANNED = ("diagnosa", "diagnosis", "prediksi", "monitoring", "pemantauan")
NEGATORS = {"bukan", "tidak", "tanpa", "not", "no", "never"}
DASH = re.compile(r"(?<=[A-Za-z])-(?=[A-Za-z])|[–—]")
CITE = re.compile(r"\[(\d+|new)\]")
CODE = re.compile(r"`[^`]*`")
WORD = re.compile(r"[A-Za-z]+")


def _negated(words, i):
    return any(w in NEGATORS for w in words[max(0, i - 4):i])


def check(text):
    problems = []
    for n, line in enumerate(text.splitlines(), 1):
        if line.strip().upper().startswith("## DAFTAR PUSTAKA"):
            break
        if line.lstrip().startswith("!["):
            continue
        body = CODE.sub("", line)
        for m in DASH.finditer(body):
            problems.append(f"line {n}: dash: {body[max(0, m.start() - 20):m.end() + 20]}")
        for m in CITE.finditer(body):
            v = m.group(1)
            if v == "new" or not 1 <= int(v) <= 41:
                problems.append(f"line {n}: citation: {m.group(0)}")
        words = [w.lower() for w in WORD.findall(body)]
        for i, w in enumerate(words):
            if w in BANNED and not _negated(words, i):
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
