#! usr/bin/env python3
# -*- coding: utf-8 -*-

# Return the sum of two given numbers
# or the concatenation of two strings
# Parameters : two numbers, or two strings
# Returns : the sum of the two given numbers,
# or the concatenation of the two given strings (first then second)
def sum(a, b):
    c = a + b
    return c

# Return the square of the given number
# (result of multiplying the number by itself)
def square(n):
    return n * n

# LOGIC (tests)
def main():
    print(sum(2,3))
    print(sum("Hello ", "World !"))
    print(square(5))

if __name__ == '__main__':
    main()
