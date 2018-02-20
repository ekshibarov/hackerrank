#!/bin/python3

import sys
import operator


def birthdayCakeCandles(n, ar):
    _, max_value = max(enumerate(ar), key=operator.itemgetter(1))
    counter = 0
    for value in ar:
        if value == max_value:
            counter += 1
    return counter


n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = birthdayCakeCandles(n, ar)
print(result)
