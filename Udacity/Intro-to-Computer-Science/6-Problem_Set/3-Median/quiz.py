#! usr/bin/env python3
# -*- coding: utf-8 -*-


# bigger
# Return the greatest of two given numbers
# Parameters : two numbers
# Returns : a number
def bigger(a, b):
    if a > b:
        return a
    return b


# biggest
# Return the largest of three given numbers
# Parameters : three numbers
# Returns : a number
def biggest(a, b, c):
    return bigger(bigger(a, b), c)


# median
# Return the median of three given numbers
# Parameters : three numbers
# Returns : one number
# NB: if two of the given values are equal,
# then whaterver migt be the third value, their common value will be outputed.
def median(a, b, c):
    highest = biggest(a, b, c)
    if a == highest:
        return bigger(b, c)
    if b == highest:
        return bigger(a, c)
    return bigger(a, b)


# LOGIC : test cases
def main():
# bigger
    # print(bigger(2, 7))
    # print(bigger(3, 2))
    # print(bigger(3, 3))
# biggest
    # print(biggest(3, 6, 9))
    # print(biggest(6, 9, 3))
    # print(biggest(9, 3, 6))
    # print(biggest(3, 3, 9))
    # print(biggest(9, 3, 9))
# median
    print(median(1, 2, 3))
    print(median(9, 3, 6))
    print(median(7, 8, 7))
    print(median(9, 9, 8))

if __name__ == '__main__':
    main()
