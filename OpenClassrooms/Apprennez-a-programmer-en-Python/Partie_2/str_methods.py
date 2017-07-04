# -*-coding:Latin-1 -*

# Mini string "formater"



# Can be improved by checking user input's validity
def choose_operation() :

    """ Ask user to choose an operation and return it."""

    return (input("Please choose one of the following operations :\n"\
                  "- capitalize\n"\
                  "- center\n"\
                  "- lower\n"\
                  "- strip\n"\
                  "- upper\n"))



def choose_size(min) :

    """Ask user to enter a size greater than min."""

    size = min - 1

    while size < min :
        size = input("Please enter the final size of your string." \
                     " It must be greater or equal to "\
                     "{current}.\n".format(current = min))
        try :
            size = int(size)
        except ValueError :
            print("You did not type a number.")
            size = min - 1
            continue

    return size



def string_formater() :

    """Ask for a string and execute required transformation."""

    string = input("Please enter your string :")
    operation = choose_operation()

    if operation == "capitalize" :
        string = string.capitalize()
    elif operation == "center" :
        final_size = choose_size(len(string))
        string = string.center(final_size)
    elif operation == "lower" :
        string = string.lower()
    elif operation == "strip" :
        string = string.strip()
    elif operation == "upper" :
        string = string.upper()
    else :
        print("Sorry, invalid operation.")

    print("Your string is :\n{}\n".format(string))



def main() :

    """Run string_formater function until user presses [Q]."""

    string = str()  # same as string = ""

    while string.lower() != "q" :
        string_formater()
        print("Press on [Q] to quit.")
        string = input()

    print ("Good bye !")



if __name__ == '__main__' :
    main()

