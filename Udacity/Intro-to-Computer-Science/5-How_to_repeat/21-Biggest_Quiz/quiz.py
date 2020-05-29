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

# LOGIC : test cases
def main():
    # bigger
    print(bigger(2, 7))
    print(bigger(3, 2))
    print(bigger(3, 3))
    # biggest
    print(biggest(3, 6, 9))
    print(biggest(6, 9, 3))
    print(biggest(9, 3, 6))
    print(biggest(3, 3, 9))
    print(biggest(9, 3, 9))

if __name__ == '__main__':
    main()
