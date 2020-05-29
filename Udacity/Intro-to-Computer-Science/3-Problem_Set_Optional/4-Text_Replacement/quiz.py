#! usr/bin/env python3
# -*- coding: utf-8 -*-

# Take a line of text and find the first occurence of a certain marker,
# and replace it with a replacement text.
# The resulting line of text is stored in the replaced variable.

marker = "AFK"
replacement = "away from keyboard"
line = "I will now go to sleep and be AFK until lunch time tomorrow."

def main():
    replaced = line[:line.find(marker)] + replacement + line[line.find(marker) + len(marker) :]
    print(replaced)

if __name__ == '__main__':
    main()
