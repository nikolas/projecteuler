#!/usr/bin/env python3

def is_palindrome(word):
   for i in range(len(word) // 2):
         if word[i] != word[-1 - i]:
             return False
   return True


def find_double_base_palindromes_to(n):
    a = []

    for i in range(n):
        if is_palindrome(str(i)) and is_palindrome(bin(i)[2:]):
            a.append(i)
        
    return a


if __name__ == '__main__':
    a = find_double_base_palindromes_to(1000000)
    print(a)
    print(sum(a))    
