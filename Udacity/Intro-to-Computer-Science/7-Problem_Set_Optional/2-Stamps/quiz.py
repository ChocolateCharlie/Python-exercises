#! usr/bin/env python3
# -*- coding: utf-8 -*-


# use_stamps
# Parameters :  an integer representing the pence
#               an integer representing the value of the used stamps
# Returns :  a tuple representing the number of stamps of that value
# used and the resting pence
def use_stamps(pence, value):
    nb_stamps = int(pence / value)
    return nb_stamps, pence - nb_stamps * value


# stamps
# Return the number of 5p, 2p and 1p stamps required to make up a given pence
# positive integer value.
# Parameters : a positive integer representing pence
# Returns :  a tuple representing the number of 5p, 2p and 1p stamps required
# This functions computes the fewest total stamps as possible.
def stamps(pence):
    stamp_5p, pence = use_stamps(pence, 5)
    stamp_2p, pence = use_stamps(pence, 2)
    stamp_1p = int(pence)
    return stamp_5p, stamp_2p, stamp_1p

# LOGIC : test cases
def main():
    print(stamps(8))
    print(stamps(5))
    print(stamps(29))
    print(stamps(0))

if __name__ == '__main__':
    main()
