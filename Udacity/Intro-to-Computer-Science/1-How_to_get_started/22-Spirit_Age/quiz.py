#! usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import logging as log

log.basicConfig(level=log.DEBUG)

# Ask user's age in years, then print it in days

def main():
    try:
        age = int(input("Please enter your age: "))
        print("You have been alive for {} days.".format(age * 365))
    except:
        e = sys.exc_info()[0]
        log.error( "Did you type your age ?\n\
Here is the error message: %s" %e)

if __name__ == '__main__':
    main()
