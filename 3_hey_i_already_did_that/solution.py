#!/usr/bin/python2.7

def to_base_b(n, b):
    n_int = int(n)
    seq = []
    while n_int >= b:
        r = n_int % b
        seq.append(str(r))
        n_int = (n_int - r) // b
    seq.append(str(n_int))
    return ''.join(seq[::-1])


def to_base_10(n, b):
    x = list(n[::-1])
    result = 0
    for i, a in enumerate(x):
        result += int(a) * (b ** i)
    return result


def solution(n, b):
    k = len(n)
    spotted = []
    while n not in spotted:
        spotted.append(n)
        sorted_l = sorted(list(n))
        x = ''.join(sorted_l[::-1])
        y = ''.join(sorted_l)
        z = str(int(x) - int(y)) if b == 10 \
            else to_base_b(str(to_base_10(x, b) - to_base_10(y, b)), b)
        n = (k - len(z)) * "0" + z
    return len(spotted) - spotted.index(n)

