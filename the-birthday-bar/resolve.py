#!/bin/python3

import sys


def solve(n, s, d, m):
    count_bars = 0
    for num in range(0, n):
        bar = s[num:num + m]
        sum_squares = sum(bar)
        if sum_squares == d:
            count_bars += 1
    return count_bars


n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
d, m = input().strip().split(' ')
d, m = [int(d), int(m)]
result = solve(n, s, d, m)
print(result)
