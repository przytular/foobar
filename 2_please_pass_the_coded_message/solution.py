#!/usr/bin/python2.7

from itertools import combinations

def solution(l):
    l.sort(reverse=True)
    l_len = len(l)
    for i in range(1, l_len + 1)[::-1]:
        for seq in combinations(l, i):
            if sum(seq) % 3 == 0:
                return int(''.join(map(str, seq)))
    return 0

