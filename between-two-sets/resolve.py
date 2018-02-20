#!/bin/python3

import sys


def getTotalX(a, b):
    start_at = a[-1]
    end_at = b[0]
    count = 0
    for x in range(start_at, end_at + 1):
        processed_a = list(filter(lambda ai: x % ai == 0, a))
        processed_b = list(filter(lambda bi: bi % x == 0, b))
        if (set(a) == set(processed_a)) and (set(b) == set(processed_b)):
            count += 1
    return count


if __name__ == "__main__":
    n, m = input().strip().split(' ')
    n, m = [int(n), int(m)]
    a = list(map(int, input().strip().split(' ')))
    b = list(map(int, input().strip().split(' ')))
    total = getTotalX(a, b)
    print(total)
