#!/usr/bin/env python3


def make_diagonal_sum_to(n):
    a = []
    diag_counter = 0
    skip = 1

    i = 1
    while i <= n:
        a.append(i)

        if diag_counter == 4:
            diag_counter = 0
            skip += 2

        i += (skip + 1)
        diag_counter += 1
            
    return a


if __name__ == '__main__':
    a = make_diagonal_sum_to(1002001)
    #print(a)
    print(sum(a))
