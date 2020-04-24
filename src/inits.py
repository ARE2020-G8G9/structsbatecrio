from tkinter import *
from tkinter.messagebox import *
import time
import math
import random
import numpy as np
from matplotlib import pyplot as plt
import displays as disp
import stats

###initialisation des paramètres et bacteries

#widget ph_opt, temp_opt, taux de croissance optimal... enfin tous les parametres mis en demande a l'utilisateur pour deux bacteries donc on indice les valeur par le type 1 ou 2 de la bacterie (ex : ph_opt2) sauf pour la temperature de la boite notee temp et son ph note ph qui prennent d'autres curseurs

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
    taux_temp = ((temp - tmax)*(temp - tmin)**2) / ((temp_opt - tmin) * (temp_opt - tmin)*(temp - temp_opt) - (temp_opt - tmax)*(temp_opt + tmin - 2*temp))
    if ph_opt <= 6:
        ph_min = 1
        ph_max = 6
    if ph_opt > 6 and ph_opt <= 8:
        ph_min = 6
        ph_max = 8
    if ph_opt > 8:
        ph_min = 7
        ph_max = 11.5
    a = ph - ph_min
    b = ph - ph_max
    c = ph - ph_opt
    taux_ph = a * b / ( a * b - c**2 )
    return taux_opt * taux_temp * taux_ph

def init_bact(num_souche, taux_opt, ph, ph_opt, temp, temp_opt):
    return {'x' : 0, 'y' : 0, 'contenu' : num_souche + 2,'dernier_repas' : 0, 'age' : 0, 'resistance' : 0, 'taux_de_croissance' : taux_de_croissance_effectif(taux_opt, ph, ph_opt, temp, temp_opt), 'capa_de_repro' : 0, 'nb_action' : 0}

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

def init_pos_bact(boite, bact, canvas):
    box = boite
    x, y = pos_alea(boite)
    box[x][y] = bact
    x0 = str(x) + 'm'
    y0 = str(y) + 'm'
    x1 = str(x + 1) + 'm'
    y1 = str(y +1) + 'm'
    
    couleur_souche = ""
    if bact['contenu'] == 3:
        couleur_souche = "red"
    elif bact['contenu'] == 4:
        couleur_souche = "blue"
        
    canvas.create_rectangle(x0, y0, x1, y1, width = 0, fill = couleur_souche)
    return box