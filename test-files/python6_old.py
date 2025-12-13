
import subprocess
import sys
import csv



def run(path, cmd):
    return subprocess.run(cmd, cwd=path, stdout=subprocess.PIPE, text=True).stdout.splitlines()

def part1(path):
    commits = run(path, ["git", "log", "--pretty=format:%H", "--reverse"])
    output = []

    for i in range(1, len(commits)):

        old, new = commits[i - 1], commits[i]
        diff = run(path, ["git", "diff", "--name-status", old, new])
        
        added, modified, deleted = [], [], []

        for line in diff:
            if not line.strip():
                continue
            

            ctype, fname = line.split("\t", 1)
            if ctype == "A": added.append(fname)
            elif ctype == "M": modified.append(fname)
            elif ctype == "D": deleted.append(fname)


