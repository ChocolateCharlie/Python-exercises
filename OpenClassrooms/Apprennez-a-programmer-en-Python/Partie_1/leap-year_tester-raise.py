# -*-coding:Latin-1 -*



# Aks user to enter a year

year = input ("Please enter a year : ")

#Verify user input

try :
    year = int(year)
    if year <= 0 :
        raise ValueError("Year cannot be inferior or equal to zero.")
except ValueError as returned_error:
    print("Invalid input : ", returned_error)


# Print whether the given year is a leap year or not

if (year % 4) or ((year % 100 == 0) and (year % 400)) :
    print (str(year) + " is not a leap year.")
else :
    print (str(year) + " is a leap year.")

