#! usr/bin/env python3
# -*- coding: utf-8 -*-

# find_second
# Return the position of the second occurrence of a given target string in a
# given search string.
# Parameters :  a search string
#               a target string
# Returns :  an integer
def find_second(search, target):
    return search.find(target, search.find(target) + 1)

# LOGIC : test cases
def main():
    danton = "De l'audace, encore de l'audace, toujours de l'audace"
    print(find_second(danton, 'audace'))

    twister = "she sells seashells by the seashore"
    print(find_second(twister, 'she'))

if __name__ == '__main__':
    main()
