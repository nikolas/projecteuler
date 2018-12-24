#!/usr/bin/env python3


def find_digit_fifth_to(n):
    ds = []
    for i in range(2, n):
        s = str(i)
        if sum([(int(x) ** 5) for x in s]) == i:
            ds.append(i)

    return ds


if __name__ == '__main__':
    a = find_digit_fifth_to(1000000)
    print(a, sum(a))
