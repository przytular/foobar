#!/usr/bin/python2.7

import string

base = ["100000", "110000", "100100", "100110", "100010", "110100", "110110", "110010", "010100", "010110"]
base.extend([x[:2]+"1"+x[3:] for x in base])
base.extend(["101001", "111001", "010111", "101101", "101111", "101011"])
alphabet = zip(string.lowercase, base)+[(" ", "000000")]


def translate(c):
    result = alphabet[next((i for i, v in enumerate(alphabet) if v[0] == c.lower()), None)][1]
    if c.isupper():
        result = "000001" + result
    return result


def solution(s):
    return ''.join([translate(i) for i in s])

