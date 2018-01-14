#! usr/bin/python3.4
# -*- coding: utf-8 -*-

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
    # get a random number
    item = my_list[0]
    # get a quote from a list
    return item

# Logic

user_answer = "A"
# Show random quote
while user_answer != "B":
    print(get_random_item_in(quotes))
    user_answer = "B"

