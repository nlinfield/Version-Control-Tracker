# Compares two versions of a file and prints which lines from the old file
# exactly match lines in the new file, using optional normalization modes

import argparse
import difflib
from pathlib import Path

# Reads a file and returns all its lines as a list
def read_lines(path: str):
    return Path(path).read_text(encoding="utf-8", errors="replace").splitlines(True)

# Cleans up each line so formatting differences don't make a false comparison
def normalize_light(lines):
    out = []
    for ln in lines:
        ln = ln.replace("\r\n", "\n").replace("\r", "\n")
        if ln.endswith("\n"):
            ln = ln[:-1]
        ln = ln.expandtabs(4).rstrip()
        out.append(ln)
    return out

# Combines wrapped text lines into full paragraphs
def normalize_prose(lines):
    out = []
    paragraph = []
    for ln in lines:
        txt = ln.strip("\r\n")
        if txt.strip() == "":
            if paragraph:
                out.append(" ".join(s.strip() for s in paragraph))
                paragraph = []
            out.append("")
        else:
            paragraph.append(txt)
        
    if paragraph:
        out.append(" ".join(s.strip() for s in paragraph))

    return out

BRACKETS = {"(": ")", "[": "]", "{": "}"}

# Combines logically connected lines of code into one line
def normalize_code(lines):
    out = []
    buf = []
    stack = []
    in_single = False
    in_double = False

    def need_more():
        if buf and buf[-1].rstrip().endswith("\\"):
            return True
        if stack or in_single or in_double:
            return True
        return False
    
    def flush():
        if buf:
            joined = " ".join(s.rstrip("\\") for s in buf)
            out.append(joined.strip())

    for ln in lines:
        raw = ln.rstrip("\n")

        for ch in raw:
            if ch == '"' and not in_single:
                in_double = not in_double
            elif ch =="'" and not in_double:
                in_single = not in_single
            elif not in_single and not in_double:
                if ch in BRACKETS:
                    stack.append(BRACKETS[ch])
                elif stack and ch == stack[-1]:
                    stack.pop()

        buf.append(raw)

        if not need_more():
            flush()
            buf = []

    flush()
    return out

# Choose what type of normalization method to use
def normalize(lines, mode):
    lines = normalize_light(lines)

    if mode == "light":
        return lines
    elif mode == "prose":
        return normalize_prose(lines)
    elif mode == "code":
        return normalize_code(lines)
    else:
        raise ValueError("Invalid normalization mode.")
    
# Prints which line of the old file matches which line of the new file
def print_line_mapping(old_lines, new_lines):
    sm = difflib.SequenceMatcher(a=old_lines, b=new_lines)

    # Only "equal" blocks mean exact lines are identical
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == "equal":
            for old_i, new_i in zip(range(i1, i2), range(j1, j2)):
                print(f"{old_i + 1}-{new_i + 1}")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("old_file", help="Old version of file")
    parser.add_argument("new_file", help="New version of file")
    parser.add_argument("--mode", choices=["light", "prose", "code"], default="light")
    args = parser.parse_args()

    old_raw = read_lines(args.old_file)
    new_raw = read_lines(args.new_file)

    old_norm = normalize(old_raw, args.mode)
    new_norm = normalize(new_raw, args.mode)

    print_line_mapping(old_norm, new_norm)

if __name__ == "__main__":
    main()