#! usr/bin/env python3
# -*- coding: utf-8 -*-

# print_numbers
# Print out all whole numbers from 1 to a positive given number
# Parameters : a number
# Returns : Nothing
# NB: if the input number is inferior at 1, nothing will be printed
def print_numbers(n):
    i = 0
    while (i < n):
        i = i + 1
        print(i)

# LOGIC : test cases
def main():
    print_numbers(3)
    print_numbers(-4)

if __name__ == '__main__':
    main()
