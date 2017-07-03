# -*-coding:Latin-1 -*

"""Multipli module, contains the following function :
    - table"""

# Table function

def table(nb, max = 10) :

    """Print the multiplication table of nb
        from 1 * nb to max * nb"""

    i = 0

    while i < max :
        print(i + 1 , " * ", nb, " = ", (i + 1) * nb)
        i += 1



# Table tests

if __name__ == "__main__" :
    help("multipli")
    table(3, 20)
    table(4)

