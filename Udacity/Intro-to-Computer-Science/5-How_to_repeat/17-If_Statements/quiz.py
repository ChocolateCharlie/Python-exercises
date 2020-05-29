#! usr/bin/env python3
# -*- coding: utf-8 -*-

# bigger
# Return the greatest of two given numbers
# Parameters : two numbers
# Returns : a number
# NB: if the two given numbers are equal,
# this function returns the value of both numbers
def bigger(a, b):
    if a > b:
        return a
    return b

# LOGIC : test cases
def main():
    print(bigger(2, 7))
    print(bigger(3, 2))
    print(bigger(3, 3))

if __name__ == '__main__':
    main()
