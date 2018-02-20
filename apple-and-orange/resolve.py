#!/bin/python3

import sys


def countApplesAndOranges(s, t, a, b, apples, oranges):
    count_apples = 0
    count_oranges = 0
    for apple in apples:
        point = a + apple
        if s <= point <= t:
            count_apples += 1
    print(count_apples)
    for orange in oranges:
        point = b + orange
        if s <= point <= t:
            count_oranges += 1
    print(count_oranges)


if __name__ == "__main__":
    s, t = input().strip().split(' ')
    s, t = [int(s), int(t)]
    a, b = input().strip().split(' ')
    a, b = [int(a), int(b)]
    m, n = input().strip().split(' ')
    m, n = [int(m), int(n)]
    apple = list(map(int, input().strip().split(' ')))
    orange = list(map(int, input().strip().split(' ')))
    countApplesAndOranges(s, t, a, b, apple, orange)
