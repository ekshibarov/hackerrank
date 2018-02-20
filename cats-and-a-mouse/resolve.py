#!/bin/python3

import sys

def catAndMouse(x, y, z):
    return "Cat A" if abs(z - x) < abs(z - y) else "Cat B" if abs(z - x) > abs(z - y) else "Mouse C"

if __name__ == "__main__":
    q = int(input().strip())
    for a0 in range(q):
        x, y, z = input().strip().split(' ')
        x, y, z = [int(x), int(y), int(z)]
        result = catAndMouse(x, y, z)
        print (" ".join(map(str, result)))


