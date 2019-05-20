#!/usr/bin/env python3
import numpy


def primes_to(n):
    """ Returns a array of primes, 3 <= p < n """
    sieve = numpy.ones(n // 2, dtype=numpy.bool)
    for i in range(3, int(n**0.5)+1, 2):
        if sieve[i // 2]:
            sieve[i * i // 2 :: i] = False
    return 2 * numpy.nonzero(sieve)[0][1::] + 1

def rotations(number):
    str_number = str(number)
    return {
        int(str_number[i:] + str_number[:i])
        for i in range(len(str_number))
    }

def is_circular_prime(primes, n):
    for x in rotations(n):
        if x not in primes:
            return False

    return True

def find_circular_primes(primes):
    circular_primes = []

    for prime in primes:
        if prime:
            if is_circular_prime(primes, prime):
                circular_primes.append(prime)

    return circular_primes

if __name__ == '__main__':
    primes = primes_to(1000000)
    circular_primes = find_circular_primes(primes)
    print(len(circular_primes) + 1)
