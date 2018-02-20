#!/bin/python3

import sys


def divisibleSumPairs(n, k, ar):
    count_div = 0
    for i in range(0, n):
        for j in range(0, n):
            if i < j and ((ar[i] + ar[j]) % k) == 0:
                count_div += 1
    return count_div


n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
ar = list(map(int, input().strip().split(' ')))
result = divisibleSumPairs(n, k, ar)
print(result)
