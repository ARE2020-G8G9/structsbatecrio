

dict_ex = {"x" : 0, "y": 0, "contenu" : 1, "dernier_repas" : 0, "age" : -1, "resistance" : -1, "taux_de_croissance" : -1, "capa_de_repro" : 0, 'nb_action' : 0}
case_vide = {"x" : 0, "y": 0, "contenu" : 0, "dernier_repas" : 0, "age" : 0, "resistance" : -1, "taux_de_croissance" : -1, "capa_de_repro" : 0, 'nb_action' : 1}
case_antibio = {"x" : 0, "y": 0, "contenu" : 2, "dernier_repas" : 0, "age" : 0, "resistance" : -1, "taux_de_croissance" : -1, "capa_de_repro" : 0, 'nb_action' : 1}

#On définit les correspondances entre les chiffres et leur signification : 0 = vide ; 1 =  nourriture ; 2 = antibiotique ; 3 = bactérie1 ; 4 = bactérie2

import tkinter
import time
import math
import random
import numpy as np
from matplotlib import pyplot as plt

import structures_complexes as sc

sc.testAjMod()

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
def pause():
    programPause = input("Press the <ENTER> key to continue...")

###initialisation des paramètres et bacteries

#widget ph_opt, temp_opt, taux de croissance optimal... enfin tous les parametres mis en demande a l'utilisateur pour deux bacteries donc on indice les valeur par le type 1 ou 2 de la bacterie (ex : ph_opt2) sauf pour la temperature de la boite notee temp et son ph note ph qui prennent d'autres curseurs

lifespawn_bact1 = 200
lifespawn_bact2 = 200
lifespawn_sans_nourriture_bact1 = 100
lifespawn_sans_nourriture_bact2 = 100
lifespawn_antibio = 100

def taux_de_croissance_effectif(taux_opt, ph, ph_opt, temp, temp_opt):
    if temp_opt <= 20:
        tmin = 0
        tmax = 20
    if temp_opt > 20 and temp_opt < 45:
        tmin = 20
        tmax = 45
    if temp_opt >= 45:
        tmin = 45
        tmax = 70
    taux_temp = ((temp - tmax)*(temp - tmin)**2) / ((temp_opt - tmin) * ((temp_opt - tmin)*(temp - temp_opt) - (temp_opt - tmax)*(temp_opt + tmin - 2*temp)))
    if ph_opt <= 6:
        ph_min = 1
        ph_max = 6
    if ph_opt > 6 and ph_opt <= 8:
        ph_min = 6
        ph_max = 8
    if ph_opt > 8:
        ph_min = 7
        ph_max = 11,5
    taux_ph = ((ph - ph_min)*(ph - ph_max)) / ((ph-ph_min)*(ph - ph_max) - (ph - ph_opt)**2)
    return taux_opt * taux_temp * taux_ph

def init_bact1(taux_opt1, ph, ph_opt1, temp, temp_opt1):
    return {'x' : 0, 'y' : 0, 'contenu' : 3,'dernier repas' : 0, 'age' : 0, 'resistance' : 0, 'taux_de_croissance' : taux_de_croissance_effectif(taux_opt1, ph, ph_opt1, temp, temp_opt1), 'capa_de_repro' : 0, 'nb_action' : 0}

def init_bact2(taux_opt2, ph, ph_opt2, temp, temp_opt2):
    return {'x' : 0, 'y' : 0, 'contenu' : 4,'dernier_repas' : 0, 'age' : 0, 'resistance' : 0, 'taux_de_croissance' : taux_de_croissance_effectif(taux_opt2, ph, ph_opt2, temp, temp_opt2), 'capa_de_repro' : 0, 'nb_action' : 0}

###Initialisation de la boite
def coo(x, y):
    return {'x' : x, 'y' : y, 'contenu' : 1,'dernier_repas' : 0, 'age' : 0, 'resistance' : -1, 'taux_de_croissance' : 0, 'capa_de_repro' : 0, 'nb_action' : 0}

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

def pos_alea(boite):
    L = len(boite);
    l = len(boite[0])
    return (random.choice(range(0, L)), random.choice(range(0, l)))

def init_pos_bact(boite, bact):
    box = boite
    x, y = pos_alea(boite)
    box[x][y] = bact
    return box

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

def in_liste(contenu, liste): #cherche si un contenu est dans une liste de dico
    for i in range(0, len(liste)):
        if contenu == liste[i]['contenu']:
            return True
    return False

def mort_bacterie(boite, x, y):
    box = boite
    box[x][y] = {"x" : x, "y": y, "contenu" : 1, 'dernier_repas' : 0, "age" : 0, "resistance" : -1, "taux_de_croissance" : -1, 'capa_de_repro' : 0, 'nb_action' : 1}
    return box

def deplacement_possible(boite, x, y):
    if boite[x][y]['contenu'] == 3 or boite[x][y]['contenu'] == 4:
        if boite[x][y]['nb_action'] != 0:
            return False
        voisinage_direct = voisinage(boite, x, y, 1)
        for i in range(0, len(voisinage_direct)):
            if (voisinage_direct[i]['contenu'] == 0 or voisinage_direct[i]['contenu'] == 1) or (boite[x][y]['resistance'] != -1 and voisinage_direct[i]['contenu'] == 2):
                return True
    return False

def distance(x0, y0, x1, y1):
    return math.sqrt((x1 - x0)**2 + (y1 - y0)**2)

def nourriture_plus_proche(boite, x, y, taille):
    voisinage0 = voisinage(boite, x, y, taille)
    if not in_liste(1, voisinage0):
        return (x, y)
    else:
        #retourner les coordonnées du "1" le plus proche dans le champ de vision de la bactérie.
        liste_1 = []
        for i in range (0, len(voisinage0)):
            if voisinage0[i]['contenu'] == 1:
                liste_1.append(voisinage0[i])
        dist_min = 1000 #on considère aucun déplacement en diagonale, les bactéries se déplace sur les cases adjacentes à la leur.
        res = (x, y)
        for i in range(0, len(liste_1)):
            xi = liste_1[i]['x']
            yi = liste_1[i]['y']
            disti = distance(x, y, xi, yi)
            if disti < dist_min:
                dist_min = disti
                res = (xi, yi)
        return res

def chemin_plus_rapide(x0, y0, x1, y1):
    """Renvoie le chemin le plus rapide de (x0, y0) à (x1, y1) dans un tuple de deplacements à effectuer"""
    return (x1 - x0, y1 - y0)

def deplacement(boite, x, y, new_x, new_y):
    box = boite
    if box[new_x][new_y]['contenu'] == 1:
        box[x][y]['dernier_repas'] = 0
    box[new_x][new_y] = box[x][y]
    box[new_x][new_y]['nb_action'] = 1
    box[x][y] = {"x" : 0, "y": 0, "contenu" : 0,"dernier_repas" : 0, "age" : 0, "resistance" : -1, "taux_de_croissance" : -1, "capa_de_repro" : 0, 'nb_action' : 1} #laisse un vide après s'être déplacée
    return box

def naissance(boite, x, y, new_x, new_y):
    box = boite
    bact_type = boite[x][y]['contenu']
    box = deplacement(boite, x, y, new_x, new_y)
    box[x][y] = {"x" : 0, "y": 0, "contenu" : bact_type,"dernier_repas" : 0, "age" : 0, "resistance" : -1, "taux_de_croissance" : -1, "capa_de_repro" : 0, "nb_action" : 1} #laisse une nouvelle bactérie après s'être déplacée
    box[new_x][new_y]['capa_de_repro'] = 0
    return box

def pos_alea_antibio(boite):
    #la goute est de hauteur et largeur max 9
    intervalle = range(0,len(boite) - 9)
    x = random.choice(intervalle)
    y = random.choice(intervalle)
    return (x, y)

def remplace_par_antibio_si_non_resis(boite, x, y):
    box = boite
    if box[x][y]['resistance'] == -1:
        box[x][y] = case_antibio
        box[x][y]['x'] = x
        box[x][y]['y'] = y
    return box

def ajout_antibio(boite, x, y):
    """je suppose qu'on prend 100 * 100 en format de boite pour faire l'echelle de la goute"""
    box = boite
    for i in range(-4, 5):
        for j in range(-4, 5):
            if distance(x, y, x + i, y + j) <= 5 and ( ( (i == -1) or (i == 1) ) and ( (j == -4) or (j == 4) ) ):
                remplace_par_antibio_si_non_resis(box, x + i, y + j)
    return box

def evo_age(boite):
    box = boite
    for i in range(0, len(box)):
        for j in range(0, len(box[0])):
            contenu = box[i][j]['contenu']
            if contenu == 2 or contenu == 3 or contenu == 4:
                box[i][j]['age']+= 1
                if contenu != 2:
                    box[i][j]['dernier_repas']+= 1
    return box

def evo_capa_de_reprod(boite):
    box = boite
    for i in range(0, len(box)):
        for j in range(0, len(box[0])):
            contenu = box[i][j]['contenu']
            if contenu == 3 or contenu == 4:
                box[i][j]['capa_de_repro']+=0.1
    return box

def death_verif_and_apply(boite):
    box = boite
    for i in range(0, len(box)):
        for j in range(0, len(box[0])):
            contenu = box[i][j]['contenu']
            age = box[i][j]['age']
            dernier_repas = box[i][j]['dernier_repas']
            if contenu == 2 and age >= lifespawn_antibio:
                box[i][j] = {"x" : x, "y": y, "contenu" : 0, 'dernier_repas' : 0, "age" : 0, "resistance" : -1, "taux_de_croissance" : -1, 'capa_de_repro' : 0, 'nb_action' : 1}
            if contenu == 3 and (age >= lifespawn_bact1 or dernier_repas >= lifespawn_sans_nourriture_bact1):
                box = mort_bacterie(box, i, j)
            if contenu == 4 and (age >= lifespawn_bact2 or dernier_repas >= lifespawn_sans_nourriture_bact2):
                box = mort_bacterie(box, i, j)
    return box

def reset_nb_action(boite):
    box = boite
    for i in range(0, len(box)):
        for j in range(0, len(box[0])):
            box[i][j]['nb_action'] = 0
    return box

### Affichage
def convert_to_array(boite):
    res = []
    for i in range(0, len(boite)):
        temp = []
        for j in range(0, len(boite[0])):
            temp.append(boite[i][j]['contenu'])
        res.append(temp)
    return np.array(res)

def plot_boite(boite):
    box = boite
    A = convert_to_array(box)
    plt.figure(figsize=(15,12)) # (30,30) = Taille de la figure
    plt.imshow(A,cmap='viridis')
    plt.colorbar()
    plt.tick_params(top=False, bottom=False, right=False, left=False, labelleft=False, labelbottom=False)
    plt.show()

###Global

def tour(boite):
    box = boite
    for i in range(0, len(box)):
        for j in range(0, len(box[0])):
            if deplacement_possible(box, i, j):
                a, b = nourriture_plus_proche(box, i,j, 1)
                case = box[i][j]
                print(case)
                if case['age'] >= 1 and case['capa_de_repro'] >= (1 - case['taux_de_croissance']):
                    box = naissance(box, i, j, a, b)
                else:
                    box = deplacement(box, i, j, a, b)
    box = evo_age(box)
    box = death_verif_and_apply(box)
    box = evo_capa_de_reprod(box)
    box = reset_nb_action(box)
    return box

def structure_bacterio(iter_max):
    temp = 25
    ph = 7
    box = init_boite(10)
    init_pos_bact(box, init_bact1(1, ph, 7, temp, 25))
    cmpt = 0
    plot_boite(box)
    while cmpt < iter_max:
        box = tour(box)
        plot_boite(box)
        cmpt+=1
        #pause()
    return None
