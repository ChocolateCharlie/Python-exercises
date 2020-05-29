#! usr/bin/env python3
# -*- coding: utf-8 -*-

# Print the distance, in meters, that light travels during one processor cycle.
# speed of light = 299 792 458 meters per second
# cycles per second = 2,7 GHz

def main():
    speed_of_light = 299792458.0
    cycles_per_second = 2700000000.0

    print(speed_of_light / cycles_per_second)

if __name__ == '__main__':
    main()
