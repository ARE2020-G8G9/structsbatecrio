from tkinter import *
from tkinter.messagebox import *
import time
import math
import random
import numpy as np
from matplotlib import pyplot as plt
import inits as ins
import displays as disp

### Statistiques
#pas mal de fonctions proches des stats de Schelling
def nombre_individus(boite):
    res = {"Bacterie1" : 0, "Bacterie2" : 0}
    for i in range(0, len(boite)):
        for j in range(0, len(boite[0])):
            contenu = boite[i][j]['contenu']
            if contenu == 3:
                res["Bacterie1"]+=1
            if contenu == 4:
                res["Bacterie2"]+=1
    return res

def nombre_nourriture_antibio(boite):
    res = {"Vide" : 0, "Nourriture" : 0, "Antibio" : 0}
    for i in range(0, len(boite)):
        for j in range(0, len(boite[0])):
            contenu = boite[i][j]['contenu']
            if contenu == 0:
                res["Vide"]+=1
            if contenu == 1:
                res["Nourriture"]+=1
            if contenu == 2:
                res["Antibio"]+=1
    return res
###Je laisse tout de même cette fonction pour la reprendre au cas où la nouvelle ne correspond pas à ce dont on a besoin
"""def affiche_courbes(iter_max):
     temp = 25
    ph = 7
    cmpt = 0
    nb_bacterie = 0
    f_antibio = 25
    f_nourriture = 20
    demi_cote = 5
    debut_ajout = 10
    box = init_boite(100)
    lsy_nb_bacterie = [0,10,20,30,40,50,60,70,80,90,100,110]
    lsx_taille = []
    lsx = []
    while cmpt < iter_max and continuer(box):
        box = tour(box)
        box = ajout(box, cmpt, f_antibio, f_nourriture, demi_cote, debut_ajout)
        lsy_nb_bacterie.append(nombre_individus(box))
        lsx_taille.append(cmpt)
        cmpt+=1
    plt.plot(lsx_taille,'bo',lsy_nb_bacterie)
    plt.ylabel("Nombre d'entités")
    plt.xlabel("Nombre d'itérations")
    plt.show()
"""

def affiche_courbes(iter_max, b1, b2, n, a, t_b, v):
    #x = np.linspace(0, iter_max, num=iter_max)
    x = [i for i in range (0, iter_max + 1)]
    #Variables globales
    """temp = 25
    ph = 7
    cmpt = 0
    nb_bacterie = 0
    f_antibio = 25
    f_nourriture = 20
    demi_cote = 5"""

    plt.plot(x, b1, label = 'souche1')
    plt.plot(x, b2, label = 'souche2')
    plt.plot(x, n, label = 'nourriture')
    plt.plot(x, a, label = 'antibio')
    plt.plot(x, t_b, label = 'total_bacteries')
    plt.plot(x, v, label = 'cases_vides')

    plt.ylabel("Nombre d'entités")
    plt.xlabel("Nombre d'itérations")
    plt.legend()
    plt.show()