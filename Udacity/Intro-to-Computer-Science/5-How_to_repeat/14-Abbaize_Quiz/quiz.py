#! usr/bin/env python3
# -*- coding: utf-8 -*-

# abbaize
# Parameters : two strings
# Returns : a string that is the first parameter, followed by two repetitions of
# the second parameter, followed by the first parameter
def abbaize(a, b):
    return a + b + b + a

# LOGIC : test cases
def main():
    print(abbaize('a', 'b'))
    print(abbaize('dog', 'cat'))

if __name__ == '__main__':
    main()
