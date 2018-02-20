#!/bin/python3

import sys

def countingValleys(n, s):
    lvl = 0
    v = 0
    for step in s:
        if step == 'U':
            lvl += 1
        if step == 'D':
            lvl -= 1
        if lvl == 0 and step =='U':
            v += 1
    return v

if __name__ == "__main__":
    n = int(input().strip())
    s = input().strip()
    result = countingValleys(n, s)
    print(result)
