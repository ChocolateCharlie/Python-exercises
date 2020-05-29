#! usr/bin/env python3
# -*- coding: utf-8 -*-

# Store the distance in meters that light travels in one nanosecond
# in the variable 'nanodistance', then print it

def main():
    speed_of_light = 299800000.
    nano_per_sec = 1000000000.

    nanodistance = speed_of_light / nano_per_sec

    print(nanodistance)

if __name__ == '__main__':
    main()
