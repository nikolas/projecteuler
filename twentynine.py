#!/usr/bin/env python3


def make_powers_array_to(n):
    ps = []

    for a in range(2, n + 1):
        for b in range(2, n + 1):
            p = a ** b
            if p not in ps:
                ps.append(p)

    return ps


if __name__ == '__main__':
    a = make_powers_array_to(100)
    print(len(a))
