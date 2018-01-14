#! usr/bin/python3.4
# -*- coding: utf-8 -*-

import random

# Data
quotes = [
        "Ecoutez-moi, Monsieur Shakespeare, nous avons beau être ou ne pas être, nous sommes !",
        "On doit pouvoir choisir entre s'écouter parler et se faire entendre."
]

characters = [
        "Alvin et les Chipmunks",
        "Babar",
        "Betty Boop",
        "Calimero",
        "Casper",
        "Le Chat Potté",
        "Kirikou"
]

# Functions

def get_random_item_in(my_list):
    rand_numb = random.randint(0, len(my_list) - 1)
    item = my_list[rand_numb]
    return item

# Logic

user_answer = "A"
# Show random quote
while user_answer != "B":
    print("{character} a dit : {quote}".format(character=get_random_item_in(characters), quote=get_random_item_in(quotes)))
    user_answer = "B"

