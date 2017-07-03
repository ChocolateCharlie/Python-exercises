# -*-coding:Latin-1 -*



# Aks user to enter a year

year = input ("Please enter a year : ")
year = int(year)


# Print whether the given year is a leap year or not

if (year % 4) or ((year % 100 == 0) and (year % 400)) :
    print (str(year) + " is not a leap year.")
else :
    print (str(year) + " is a leap year.")

