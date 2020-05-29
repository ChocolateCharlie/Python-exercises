#! usr/bin/env python3
# -*- coding: utf-8 -*-

# countdown
# Print out a countdown from a given number to one, followed by 'Blastoff!'
# Parameters :  a positive whole number
# Returns : Nothing
# The countdown is printed on separated lines.
# If the given number is inferior at one, only 'Blastoff!' will be printed.
def countdown(n):
    while n > 0:
        print(n)
        n = n - 1
    print("Blastoff!")

# LOGIC : test cases
def main():
    countdown(3)
    countdown(-1)

if __name__ == '__main__':
    main()
