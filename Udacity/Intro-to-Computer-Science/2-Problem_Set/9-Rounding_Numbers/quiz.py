#! usr/bin/env python3
# -*- coding: utf-8 -*-

# Given a variable x that stores the value of any decimal number,
# print the nearest whole number to x.
# If x is exactly half way between two whole numbers, round up.
# We assume x is not negative.

x = 3.14159
# Add previously 0.5 is for the rounding
x = x + 0.5

def main():
    x_string = str(x)
    print(x_string[:x_string.find('.')])

if __name__ == '__main__':
    main()
