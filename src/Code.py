

case = {"x" : 1, "y" : 1, "contenu" : 132456798, "age" : 132, "resitance" : 1313, "taux_de_croissance" : 0.5}
dict_ex = {"x" : 0, "y": 0, "contenu" : 1, "age" : -1, "resistance" : -1, "taux_de_croissance" : -1}

#On définit les correspondances entre les chiffres et leur signification : 0 = vide ; 1 =  nourriture ; 2 = antibiotique ; 3 = bactérie1 ; 4 = bactérie2

import random
import numpy as np

import structures_complexes as sc

structures_complexes.testAjMod()

#tests de l'initialisation des classes

"""
bacteria = sc.Bacterie()
print(bacteria.souche)
print(bacteria.symb)
print(bacteria.x)
print(bacteria.y)
print(bacteria.age)
print(bacteria.resistance)
print(bacteria.taux_de_croissance)
"""

###Initialisation de la boite
def coo(x, y):
    return {'x' : x, 'y' : y, 'contenu' : 1, 'age' : 0, 'resistance' : -1, 'taux_croissance' : 0}

def L_dico(k, L):
    res = []
    for i in range(0, L):
        res.append(coo(k, i))
    return res

def init_boite(L):
    res = []
    for i in range(0,L):
        res.append(L_dico(i, L))
    return res

def pos_aléa(boite):
    L = len(boite);
    l = len(boite[0])
    return (random.choice(range(0, L)), random.choice(range(0, l)))

###Trouver le voisinage (à tester avec le dico)(semble marcher quand meme)



def voisinage(boite, x, y, taille) :
    res = []
    if x + taille < len(boite) and x - taille >= 0:
        if y - taille >= 0 and y + taille < len(boite[0]):
            for i in range(-taille, taille + 1):
                for j in range(- taille, taille + 1):
                    if i == 0:
                        if j != 0:
                            res.append(boite[x + i][y + j])
                    else:
                        res.append(boite[x + i][y + j])
        if y - taille < 0:
            for i in range(-taille, taille + 1):
                for j in range(0, taille + 1):
                    if i == 0:
                        if j != 0:
                            res.append(boite[x + i][y + j])
                    else:
                        res.append(boite[x + i][y + j])
        if y + taille >= len(boite[0]):
            for i in range(-taille, taille + 1):
                for j in range(- taille, 1):
                    if i == 0:
                        if j != 0:
                            res.append(boite[x + i][y + j])
                    else:
                        res.append(boite[x + i][y + j])

    if x + taille >= len(boite) and x - taille >= 0:
        if y - taille >= 0 and y + taille < len(boite[0]):
            for i in range(-taille, 1):
                for j in range(- taille, taille + 1):
                    if i == 0:
                        if j != 0:
                            res.append(boite[x + i][y + j])
                    else:
                        res.append(boite[x + i][y + j])
        if y - taille < 0:
            for i in range(-taille, 1):
                for j in range(0, taille + 1):
                    if i == 0:
                        if j != 0:
                            res.append(boite[x + i][y + j])
                    else:
                        res.append(boite[x + i][y + j])
        if y + taille >= len(boite[0]):
            for i in range(-taille, 1):
                for j in range(-taille, 1):
                    if i == 0:
                        if j != 0:
                            res.append(boite[x + i][y + j])
                    else:
                        res.append(boite[x + i][y + j])

    if x + taille < len(boite) and x - taille < 0:
        if y - taille >= 0 and y + taille < len(boite[0]):
            for i in range(0, taille + 1):
                for j in range(- taille, taille + 1):
                    if i == 0:
                        if j != 0:
                            res.append(boite[x + i][y + j])
                    else:
                        res.append(boite[x + i][y + j])
        if y - taille < 0:
            for i in range(0, taille + 1):
                for j in range(0, taille + 1):
                    if i == 0:
                        if j != 0:
                            res.append(boite[x + i][y + j])
                    else:
                        res.append(boite[x + i][y + j])
        if y + taille >= len(boite[0]):
            for i in range(0, taille + 1):
                for j in range(- taille, 1):
                    if i == 0:
                        if j != 0:
                            res.append(boite[x + i][y + j])
                    else:
                        res.append(boite[x + i][y + j])
    return res



###Evolution du système (à changer avec les dico)

def in_liste(n, liste):
    for i in range(0, len(liste)):
        if n == liste[i]:
            return True
    return False

def mort_bacterie(boite, x, y):
    boite[x][y]['contenu'] = 0
    return boite

def déplacement_possible(boite, x, y, taille):
    voisinage_direct = voisinage(boite, x, y, 1)
    for i in range(0, len(voisinage_direct)):
        if voisinage_direct[i]['contenu'] == 0 or voisinage_direct[i]['contenu'] == 1:
            return True
    return False

def nourriture_plus_proche(boite, x, y, taille):
    if not in_liste(1, voisinage(boite, x, y, taille)):
        return -1
    else:
        #retourner les coordonnées du "1" le plus proche dans le champ de vision de la bactérie.
        return None

def deplacement(boite, x, y, new_x, new_y):
    boite[new_x][new_y] = boite[x][y]
    boite[x][y] = 0 #laisse un vide après s'être déplacée
    return boite

def naissance(boite, x, y, new_x, new_y):
    temp = boite[x][y]
    boite[new_x][new_y] = boite[x][y]
    boite[x][y] = temp #laisse une nouvelle bactérie après s'être déplacée
    return boite



