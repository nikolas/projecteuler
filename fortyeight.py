#!/usr/bin/env python3

def calc():
    x = 0
    for i in range(1, 1001):
        x += i ** i
    return x

if __name__ == '__main__':
    print(calc())
