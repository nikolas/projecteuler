#!/usr/bin/env python3

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
    for i in range(x):
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
    for idx, i in enumerate(abundants):
        for j in abundants[idx:]:
            if (i + j) == x and i != j:
                return True

    return False

def find_non_abundant_nums_to(x):
    nums = []
    abundants = []

    fname = 'abundants.txt'
    if True or not exists(fname):
        print('Finding abundants...')
        abundants = find_abundants_to(x)
        with open(fname, 'wb') as f:
            pickle.dump(abundants, f)
    else:
        print('Loading abundants from {}'.format(fname))
        with open(fname, 'rb') as f:
            abundants = pickle.load(f)

    for i in range(x):
        if not is_abundant_sum(i, abundants):
            print('{} is non-abundant.'.format(i))
            nums.append(i)

    return nums

if __name__ == '__main__':
    print(sum(find_non_abundant_nums_to(16000)))
