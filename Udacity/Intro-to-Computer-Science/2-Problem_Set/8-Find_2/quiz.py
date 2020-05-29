#! usr/bin/env python3
# -*- coding: utf-8 -*-

# Assume text is a variable that holds a string.
# Print the position of the second occurrence of 'zip' in text,
# or -1 if it does not occur at least twice.

text = "all zip files are zipped"

def main():
    print(text.find('zip', text.find('zip') + 1))

if __name__ == '__main__':
    main()
