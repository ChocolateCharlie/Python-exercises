#! usr/bin/env python3
# -*- coding: utf-8 -*-

# Return the sum of three given numbers, or concatenate three given strings.
# Parameters : three numbers, or three strings
# Returns : the sum of the three given numbers,
# or the concatenation of the three given strings
# (for strings, be careful on the order of the parameters)
def sum3(a, b, c):
    return a + b + c

# LOGIC : test cases
def main():
    print(sum3(1, 2, 3))
    print(sum3(93, 53, 70))

if __name__ == '__main__':
    main()
