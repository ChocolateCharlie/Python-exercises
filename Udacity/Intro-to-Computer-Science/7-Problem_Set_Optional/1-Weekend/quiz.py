#! usr/bin/env python3
# -*- coding: utf-8 -*-

# weekend
# Return True if a given string is 'Saturday' or 'Sunday', False otherwise
# Parameters : a string
# Returns : a boolean
def weekend(day):
    return day == 'Saturday' or day == 'Sunday'

# LOGIC : test cases
def main():
    print(weekend("Monday"))
    print(weekend("Saturday"))
    print(weekend("July"))
    print(weekend("Sunday"))

if __name__ == '__main__':
    main()
