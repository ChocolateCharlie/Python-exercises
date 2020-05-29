#! usr/bin/env python3
# -*- coding: utf-8 -*-

# is_friend
# Return a boolean indicating if a given string is the name of a friend.
# Assume a friend is anyone whose name starts with D, and no one else.
# Parameters : a string representing a name
# Returns : a boolean, True if it's a friend, False otherwise
# NB: the lowercase 'd' is not tested
def is_friend(name):
    try:
        return name[0] == 'D'
    except:
        return False

# LOGIC : test cases
def main():
    print(is_friend('Diane'))
    print(is_friend('Fred'))
    print(is_friend(3))

if __name__ == '__main__':
    main()
