#!/bin/python3

import sys


def breakingRecords(score):
    highest_score = score[0]
    lowest_score = score[0]
    count_lowest = 0
    count_highest = 0
    for points in score[1:]:
        if points > highest_score:
            highest_score = points
            count_highest += 1
        if points < lowest_score:
            lowest_score = points
            count_lowest += 1
    return [count_highest, count_lowest]


if __name__ == "__main__":
    n = int(input().strip())
    score = list(map(int, input().strip().split(' ')))
    result = breakingRecords(score)
    print(" ".join(map(str, result)))
