#! usr/bin/python3.4
# -*- coding: utf-8 -*-

import random
import json

##### DATA FUNCTIONS #####

# Return a list given a JSON file and key
def read_values_from_json(path, key):
    values = []
    with open(path) as f:
        data = json.load(f)
        for entry in data:
            values.append(entry[key])
        return values

# Clean a given list of strings
def clean_strings(sentences):
    cleaned = []
    for sentence in sentences:
        cleaned.append(sentence.strip())
    return cleaned

# Return a random item from a given list
def random_item_in(my_list):
    rand_numb = random.randint(0, len(my_list) - 1)
    return my_list[rand_numb]

# Return a random value from a given JSON file, given a key
def random_value(source_path, key):
    all_values = read_values_from_json(source_path, key)
    clean_values = clean_strings(all_values)
    return random_item_in(clean_values)

##### CHARACTERS AND QUOTES #####

# Gather characters from Wikipedia
def random_character():
    return random_value("characters.json", "character")

# Gather quotes from San Antonio
def random_quote():
    return random_value("quotes.json", "quote")

# Print a random sentence
def print_random_sentence():
    rand_quote = random_quote()
    rand_character = random_character()
    print(">>>>> {character} a dit : {quote}".format(character=rand_character, quote=rand_quote))

##### LOGIC #####

def main_loop():
    while True:
        print_random_sentence()
        message = ( "Voulez-vous voir une autre citation ? "
                    "Pour sortir du programme, tapez [S].")
        choice = input(message).upper()
        if choice == 'S':
            break

if __name__ == '__main__':
    main_loop()

