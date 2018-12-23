#!/usr/bin/env python3

from itertools import permutations
from string import digits


if __name__ == '__main__':
    p = list(permutations(digits, len(digits)))
    print(''.join(p[999999]))
