#!/bin/python3

import sys

def sockMerchant(n, ar):
    socks = {}
    pairs = 0
    for sock in ar:
        if sock in socks:
            pairs += 1
            del socks[sock]
        else:
            socks[sock] = sock
    return pairs



n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = sockMerchant(n, ar)
print(result)
