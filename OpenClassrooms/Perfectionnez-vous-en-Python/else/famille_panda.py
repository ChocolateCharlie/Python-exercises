#! usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd

####### NUMPY #######

# Creation d'un panda
un_panda = [100, 5, 20, 80] # pattes, poils, queue, ventre
un_panda_numpy = np.array(un_panda)

# Creation d'un bebe panda
k = 2
un_bebe_panda_numpy = un_panda_numpy / k

# Creation d'une famille panda
famille_panda = [
        [100, 5, 20, 80],   # maman panda
        [50, 2.5, 10, 40],  # bebe panda
        [110, 6, 22, 80]    # papa panda
        ]
famille_panda_numpy = np.array(famille_panda)

# Afficher la taille des pattes
print("Taille des pattes de papa panda : {}".format(famille_panda_numpy[2, 0]))
pattes = famille_panda_numpy[:, 0]
print("Taille des pattes de toute la famille :\n{}".format(pattes))
print("Somme de la taille des pattes de toute la famille : {}".format(pattes.sum()))

####### PANDAS #######

# Creation d'une famille panda
famille_panda_df = pd.DataFrame(famille_panda_numpy,
                                index = ['maman', 'bebe', 'papa'],
                                columns = ['pattes', 'poil', 'queue', 'ventre'])

# Parcours de la famille panda
for ligne in famille_panda_df.iterrows():
    index_ligne = ligne[0]
    contenu_ligne = ligne[1]
    print("Voici le panda %s :" % index_ligne)
    print(contenu_ligne)
    print("----------")

# Recherche du panda de diametre du ventre 80cm
masque = famille_panda_df["ventre"] == 80
pandas_80 = famille_panda_df[masque]
print(pandas_80)
print(famille_panda_df[~masque])

# Ajout de pandas
quelques_pandas = pd.DataFrame([[105, 4, 19, 80], [100, 5, 20, 80]],
                                columns = famille_panda_df.columns)
tous_les_pandas = famille_panda_df.append(quelques_pandas)
print(tous_les_pandas.drop_duplicates())

