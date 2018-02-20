#!/bin/python3

import sys


def migratoryBirds(n, ar):
    count_flock = dict.fromkeys(range(1, 6), 0)
    for type_bird in ar:
        count_flock[type_bird] += 1
    max_number = max(count_flock, key=count_flock.get)
    return max_number


n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = migratoryBirds(n, ar)
print(result)
