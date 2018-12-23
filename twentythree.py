#!/usr/bin/env python3

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
    cutoff = len(abundants)
    for i in abundants:
        if i > x:
            cutoff = i
            break

    return abundants[:cutoff]


def is_abundant_sum(x, abundants):
    abundants = limit_abundants(x, abundants)
    for i in abundants:
        for j in range(len(abundants)):
            el = abundants[-j]
            if i != el and (i + el) == x:
                return True

    return False

def find_non_abundant_nums_to(x):
    nums = []
    abundants = find_abundants_to(x)
    for i in range(x):
        if not is_abundant_sum(i, abundants):
            print('appending %d' % i)
            nums.append(i)

    return nums

if __name__ == '__main__':
    print(sum(find_non_abundant_nums_to(28123)))
