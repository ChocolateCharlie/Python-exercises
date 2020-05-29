#! usr/bin/env python3
# -*- coding: utf-8 -*-

# Return the factorial of a given number
# Parameters : a number
# Returns : a number
# WARNING: passing in a number inferior or equal at 1 returns 1
def factorial(n):
    ret_f = 1
    while n > 1:
        ret_f = ret_f * n
        n = n - 1
    return ret_f

# LOGIC : test cases
def main():
    print(factorial(4))
    print(factorial(5))
    print(factorial(6))

if __name__ == '__main__':
    main()
