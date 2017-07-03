# -*-coding:Latin-1 -*

from random import randrange
from math import ceil

# zCasino : a simplified shell roulette game



def ask_player() :

    """Ask player if s.he wants to play again and return boolean."""

    answer = input("Do you want to play again (y/n) ?")

    if (answer == "n") or (answer == "N") :
        return False
    else :
        return True



def enter_value (min, max) :

    """Ask player to choose a number between min and max included, return this number."""

    number = min - 1

    while (number < min) or (number > max) :
        number = input("Please enter your value (between " + str(min) + " and " + str(max) + " included) : ")

        try :
            number = int(number)
        except ValueError :
            print("You did not type a number.")
            number = min - 1
            continue

        if number < min :
            print("It's too small.")
        elif number > max :
            print("It's too big.")

    return number



def play (money) :

    """Ask player to bet some money on a number, return the amount of money after the game."""

    print("Let's choose a number !")
    bet_number = enter_value(0, 49)
    print("Now choose an amount of money !")
    bet_money = enter_value(0, money)

    money += roulette(bet_number, bet_money)
    print("You now have ", money, "$")

    return money



def roulette (bet_number, bet_money):

    """Generate a winning number and return gain of player."""

    winning_number = randrange(50)
    print("And the winning number is... ", winning_number, " !")

    if bet_number == winning_number :
        print("Congratulations ! You won ", bet_money * 3, "$ !")
        return bet_money * 3
    elif (bet_number % 2) == (winning_number % 2) :
        print("Not that bad, you get ", ceil(bet_money / 2), "$ .")
        return ceil(bet_money / 2)
    else :
        print("Awww, you lost ", bet_money, "$ ...")
        return (-bet_money)



def main_loop() :

    """Play while player has money and wants to."""

    money = 1000
    keep_playing = True

    while keep_playing :
        money = play(money)
        if money <= 0 :
            print("Just to bad, you have no more money !")
            keep_playing = False
        else :
            keep_playing = ask_player()

    print("Good bye !")



if __name__ == '__main__' :
    main_loop()

