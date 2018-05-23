#!/bin/python3

import sys

def hurdleRace(k, height):
    return  max(max(height)-k,0)

if __name__ == "__main__":
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    height = list(map(int, input().strip().split(' ')))
    result = hurdleRace(k, height)
    print(result)
