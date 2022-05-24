import random


MIN = 0
MAX = 10


nb_a_deviner = random.randint(MIN, MAX)


def ask_number(nb_min, nb_max):
    while True:
        # On entre dans une boucle infinie

        # On demande la saisie d'un nombre
        nombre = input("Saisissez un nombre entre {} et {}: ".format(nb_min, nb_max))

        try:
            nombre = int(nombre)
        except:
            pass
        else:
            # Faire la comparaison
            if nb_min <= nombre <= nb_max:
                # On a ce que l'on veut, on quitte la boucle
                return nombre


while True:
    nb_saisi = ask_number(MIN, MAX)

    if nb_saisi == nb_a_deviner:
        print("gagné")
        break
    elif nb_saisi > nb_a_deviner:
        print("Trop grand")
    else:
        print("Trop petit")

