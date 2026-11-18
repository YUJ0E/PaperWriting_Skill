#!/usr/bin/env python3
"""List paragraph-ending lines with only one or two words in a compiled paper PDF.

Usage: python3 check_orphans.py paper.pdf [--max-words 2]

Uses `pdftotext -layout`. A line counts as a paragraph end when the next line is blank,
indented (new paragraph), or the page ends. This is a heuristic: confirm each hit against
the .tex before editing, and skip headings, equations, captions, and table cells.
Two-column layouts are split at the widest gap so each column is checked on its own.
"""
import argparse
import re
import subprocess
import sys


def columns(page):
    lines = page.split("\n")
    width = max((len(l) for l in lines), default=0)
    if width < 60:
        return [lines]
    # Find a column split: a character position that is a space in most non-empty lines.
    mid_lo, mid_hi = int(width * 0.35), int(width * 0.65)
    nonempty = [l for l in lines if l.strip()]
    best, best_score = None, 0.0
    for c in range(mid_lo, mid_hi):
        score = sum(1 for l in nonempty if len(l) <= c or l[c] == " ") / max(len(nonempty), 1)
        if score > best_score:
            best, best_score = c, score
    if best is None or best_score < 0.9:
        return [lines]
    left = [l[:best].rstrip() for l in lines]
    right = [l[best:].rstrip() if len(l) > best else "" for l in lines]
    return [left, right]


def words(line):
    return re.findall(r"[A-Za-z0-9][\w\-\.\%\$]*", line)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pdf")
    ap.add_argument("--max-words", type=int, default=2)
    a = ap.parse_args()
    text = subprocess.run(["pdftotext", "-layout", a.pdf, "-"],
                          capture_output=True, text=True, check=True).stdout
    hits = 0
    for pno, page in enumerate(text.split("\f"), 1):
        for col in columns(page):
            body = [l for l in col]
            indents = [len(l) - len(l.lstrip()) for l in body if l.strip()]
            base = min(indents) if indents else 0
            for i, line in enumerate(body):
                s = line.strip()
                w = words(s)
                if not s or len(w) == 0 or len(w) > a.max_words:
                    continue
                if not s.endswith((".", ")", "]")):
                    continue  # paragraph ends normally finish a sentence
                prev = body[i - 1].strip() if i > 0 else ""
                if len(words(prev)) < 6:
                    continue  # isolated short lines are headings, labels, or equations
                nxt = body[i + 1] if i + 1 < len(body) else ""
                nxt_indent = len(nxt) - len(nxt.lstrip())
                if nxt.strip() and nxt_indent <= base + 1:
                    continue  # paragraph continues on the next line
                hits += 1
                print(f"p{pno}: ...{prev[-50:]} / {s}")
    print(f"{hits} possible orphan line(s).", file=sys.stderr)


if __name__ == "__main__":
    main()
