
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


