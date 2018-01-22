#!/usr/bin/env python3
# -*- coding: utf-8 -*-



################################################################################
################################ NUMBERS #######################################
################################################################################

print("----- Simple operations -----")
print(2 + 2)
print(50 - 5 * 6)
print((50 - 5 * 6) / 4)
print (8 / 5) # division always returns a floating point number

print("----- Divisions and remainders -----")
print(17 / 3) # classic division returns a float
print(17 // 3) # floor division discards the fractional part
print(17 % 3) # modulo

print("----- Powers -----")
print(5 ** 2)
print(2 ** 7)

print("----- Equal sign -----")
width = 20
height = 5 * 9
print(width * height)

print("----- Mixed type operands -----")
print(4 * 3.75 - 1)

################################################################################
################################# STRINGS ######################################
################################################################################

print("----- Simple strings -----")
print('simple quotes')
print("double quotes")

print("----- Raw strings -----")
print('C:\some\name')
print(r'C:\some\name')

print("----- String literals -----")
print("""\
Usage: thingy [OPTIONS]
    -h                  Display this usage message
    -H hostname         Hostname to connect to
""")
print('''Prevent \
adding a \
new line.\
''')

print("----- String concatenation -----")
print(3 * 'un' + 'ium')
print('Py' 'thon')
text = ('Put several strings within parentheses '
        'to have them joined together.')
print(text) # This only works with literals, not with variables or expressions
prefix = 'Py'
print(prefix + 'thon')

print("----- Indexing strings -----")
# NB : a character is a string of size one
word = 'Python'
print(word[0])
print(word[5])
print(word[-1]) # Start counting from the right ; -0 is the same as 0

print("----- Slicing strings -----")
print(word[0:2])
print(word[2:5])
# NB : the start is always included, and the end always excluded
# This makes sure that s[:i] + s[i:] is always equal to s
print(word[:2])
print(word[4:])
print(word[-2:])
# Out of range slice indexes are handled
print(word[4:42])
print(word[42:])

# Python strings are immutable :
# assigning to an indexed position results in an error.

print("----- Create new strings -----")
print('J' + word[1:])
print(word[:2] + 'py')

print("----- Built-in len() function -----")
s = 'supercalifragilisticexpialidocious'
print(len(s))

################################################################################
################################## LISTS #######################################
################################################################################

