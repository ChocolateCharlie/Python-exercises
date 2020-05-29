#! usr/bin/env python3
# -*- coding: utf-8 -*-

# udacify
# Return a string that is an uppercase 'U' followed by the input string
# Parameters : a string
# Returns : a string
def udacify(s):
    return 'U' + s

# LOGIC : test cases
def main():
    print(udacify('dacians'))
    print(udacify('turn'))
    print(udacify('boat'))

if __name__ == '__main__':
    main()
