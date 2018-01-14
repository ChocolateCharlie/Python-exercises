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
    print(item)
    return "program is over"

# Logic

user_answer = input('Tapez [Entree] pour decouvrir une autre citation ou B pour quitter le programe.')
# Show random quote
if user_answer == "B":
    pass
else:
    print(get_random_item_in(quotes))

