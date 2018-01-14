#! usr/bin/python3.4
# -*- coding: utf-8 -*-

import random
import json

# Functions

def read_values_from_json(file, key):
    values = []
    with open(file) as f:
        data = json.load(f)
        for entry in data:
            values.append(entry[key])
    return values

def get_random_item_in(my_list):
    rand_numb = random.randint(0, len(my_list) - 1)
    item = my_list[rand_numb]
    return item

def get_random_character():
    all_values = read_values_from_json("characters.json", "character")
    return get_random_item_in(all_values)

def get_random_quote():
    all_values = read_values_from_json("quotes.json", "quote")
    return get_random_item_in(all_values)

# Logic

user_answer = "A"
# Show random quote
while user_answer != "B":
    user_answer = input("{character} a dit : {quote}".format(character=get_random_character(), quote=get_random_quote()))

