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


# smaller
# Returns the smallest of two given numbers
# Parameters : two numbers
# Returns :  a number
def smaller(a, b):
    if a < b:
        return a
    return b


# biggest
# Return the largest of three given numbers
# Parameters : three numbers
# Returns : a number
def biggest(a, b, c):
    return bigger(bigger(a, b), c)


# smallest
# Return the smallest of three given numbers
# Parameters : three numbers
# Returns : a number
def smallest(a, b, c):
    return smaller(smaller(a, b), c)


# set_range
# Return the range of three given numbers
# (the range is the maximum value minus the minimum)
# Parameters : three numbers
# Returns : one number
def set_range(a, b, c):
    return biggest(a, b, c) - smallest(a, b, c)


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
# set_range
    print(set_range(10, 4, 7))
    print(set_range(1.1, 7.4, 18.7))


if __name__ == '__main__':
    main()
