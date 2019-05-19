#!/usr/bin/env python3

def digital_sum(n):
    if n < 10:
        return n
    return n % 10 + digital_sum(n // 10)

def find_digital_sum():
    n = 0

    for a in range(100):
        for b in range(100):
            d = digital_sum(a ** b)
            if d > n:
                n = d

    return n

if __name__ == '__main__':
    print(find_digital_sum())
