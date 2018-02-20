#!/bin/python3

import sys
from operator import add


def getMoneySpent(keyboards, drives, s):
    sum = []
    for k in keyboards:
        for d in drives:
            price = k + d
            if price <= s:
                sum.append(price)
    if len(sum) > 0:
        return max(sum)
    else:
        return -1

s,n,m = input().strip().split(' ')
s,n,m = [int(s),int(n),int(m)]
keyboards = list(map(int, input().strip().split(' ')))
drives = list(map(int, input().strip().split(' ')))
#  The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
moneySpent = getMoneySpent(keyboards, drives, s)
print(moneySpent)
