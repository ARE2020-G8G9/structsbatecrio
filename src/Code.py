lt = 5
Lt = 5
test = [[1, 1, 1, 1 ,1 ,1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]

case = {x : 1, y : 1, contenu : 132456798}
bactérie_test = {x : 2, y : 2, age : 1, resistance = 0, famille : 1}
antiobio_test = {x : 3, y : 3, age : 1, compatibilité : 1}

#On définit les correspondances entre les chiffres et leur signification : 0 = vide ; 1 =  nourriture ; 2 = antibiotique ; 3 = bactérie1 ; 4 = bactérie2

import random
import numpy as np

def init_boite(l, L):
    res = [l * [1]] * L
    return res

def in_liste(n, liste):
    for i in range(0, len(liste)):
        if n == liste[i]:
            return True
    return False

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

def pos_aléa(boite):
    L = len(boite);
    l = len(boite[0])
    return (random.choice(range(0, L)), random.choice(range(0, l)))

def mort_bacterie(boite, x, y):
    boite[x][y] = 0
    return boite

def déplacement_possible(boite, x, y, taille):
    voisinage_direct = voisinage(boite, x, y, 1)
    for i in range(0, len(voisinage_direct)):
        if voisinage_direct[i] == 0 or voisinage_direct[i] == 1:
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
    boite[new_x][new_y] = boite[x][y]
    boite[x][y] = 1 #laisse une nouvelle bactérie après s'être déplacée
    return boite



