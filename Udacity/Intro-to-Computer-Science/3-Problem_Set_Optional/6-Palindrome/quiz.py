#! usr/bin/env python3
# -*- coding: utf-8 -*-

# Check if a word is a palindrome.
# Print 0 if the word is a palindrome,
# print -1 otherwise
# NB: case sensitive checking
# WARNING: The word must be at least one character long.

word = "madam"

def main():
    is_palindrome = word[::-1].find(word)
    print(is_palindrome)

if __name__ == '__main__':
    main()
