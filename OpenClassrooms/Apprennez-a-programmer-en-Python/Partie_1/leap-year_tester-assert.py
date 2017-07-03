# -*-coding:Latin-1 -*



# Aks user to enter a year

year = input ("Please enter a year : ")

# Verify user input

try:
    year = int(year)
    assert year > 0
except ValueError :
    print("You did not type a number.")
except AssertionError :
    print("The year you typed is inferior or equal to zero.")



# Print whether the given year is a leap year or not

if (year % 4) or ((year % 100 == 0) and (year % 400)) :
    print (str(year) + " is not a leap year.")
else :
    print (str(year) + " is a leap year.")

