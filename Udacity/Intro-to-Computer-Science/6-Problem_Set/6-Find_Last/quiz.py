#! usr/bin/env python3
# -*- coding: utf-8 -*-

# find_last
# Return the last position in a given search string where a given target string
# appears, or -1 if there are no occurrences.
# Parameters :  a string, where the target will be searched
#               a string, the target to search
# Returns :  a number, the position of the last occurrence of the target string
# in the search string
def find_last(s, target):
    ret_last = -1
    while True:
        pos = s.find(target, ret_last + 1)
        if pos == -1:
            return ret_last
        ret_last = pos

# LOGIC : test cases
def main():
    print(find_last('aaaa', 'a'))
    print(find_last('aaaaa', 'aa'))
    print(find_last("111111111", "1"))
    print(find_last("222222222", ""))
    print(find_last("", "3"))
    print(find_last("", ""))

if __name__ == '__main__':
    main()
