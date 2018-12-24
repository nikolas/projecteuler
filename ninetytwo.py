#!/usr/bin/env python3


def nextchain(n):
    s = str(n)

    summ = 0
    for x in s:
        summ += int(x) ** 2

    return summ


def find_square_chains_to(n):
    total = 0

    for i in range(1, n):
        if i % 10000 == 0:
            print(i, total)

        c = i
        while c != 1:
            if c == 89:
                total += 1
                break

            c = nextchain(c)

    return total


if __name__ == '__main__':
    chains = find_square_chains_to(10000000)
    print('done', chains)
