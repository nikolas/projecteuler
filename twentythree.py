#!/usr/bin/env python3

from itertools import combinations
import pickle
from os.path import exists

def is_divisor(x, y):
    if y == 0:
        return False
    return x % y == 0

def find_divisors(x):
    divisors = []
    for i in range((x // 2) + 1):
        if is_divisor(x, i):
            divisors.append(i)

    return divisors

def is_abundant(x):
    return x < sum(find_divisors(x))

def find_abundants_to(x):
    nums = []
    for i in range(x + 1):
        if is_abundant(i):
            nums.append(i)

    return nums

def limit_abundants(x, abundants):
    for idx, i in enumerate(abundants):
        if i >= x:
            return idx

    return len(abundants)

def is_abundant_sum(x, abundants):
    if x > 100 and x % 2 == 0:
        return True

    abundants = abundants[:limit_abundants(x, abundants)]
    for n, m in combinations(abundants, 2):
        if n + n == x or m + m == x or n + m == x:
            return True

        if n + m > x and m + m > x and n + n > x:
            return False

    return False

def find_non_abundant_nums_to(x):
    nums = []
    abundants = []

    fname = 'abundants.txt'
    if not exists(fname):
        print('Finding abundants...')
        abundants = find_abundants_to(x)
        with open(fname, 'wb') as f:
            pickle.dump(abundants, f)
    else:
        print('Loading abundants from {}'.format(fname))
        with open(fname, 'rb') as f:
            abundants = pickle.load(f)

    print(abundants[:10])

    total = 0
    for i in range(1, x + 1):
        if i % 100 == 0:
            print('---> {} <---'.format(i))

        half_i = i // 2
        if not is_abundant_sum(i, abundants[:half_i]):
            nums.append(i)
            total += i
            print('{} is a non-abundant sum. Running total: {}'.format(
                i, total))

    return nums

if __name__ == '__main__':
    print(sum(find_non_abundant_nums_to(28123)))
