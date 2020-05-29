from enum import Enum
import numpy

class Strategy(Enum):
    CHANGE = 1
    KEEP = 2 # GARDER

def play (strategy, nb_games):
    players_choices = numpy.random.randint(0, 3, nb_games)
    winning_doors = numpy.random.randint(0, 3, nb_games)
    
    if strategy == Strategy.KEEP:
        return players_choices == winning_doors
    elif strategy == Strategy.CHANGE:
        return players_choices != winning_doors
    else:
        raise ValueError("Unknown Strategy")