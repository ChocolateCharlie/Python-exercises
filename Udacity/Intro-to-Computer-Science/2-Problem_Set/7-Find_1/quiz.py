#! usr/bin/env python3
# -*- coding: utf-8 -*-

# Assume text is a variable that holds a string.
# Print the position of the first occurrence of 'hoo' in the value of text,
# or -1 if it does not occur at all.

text = "first hoo"

def main():
    print(text.find('hoo'))

if __name__ == '__main__':
    main()
