#NE JAMAIS UTILISER CES DICO POUR REMPLACER LE CONTENU D'UNE CASE ! JAMAIS
dict_ex = {"x" : 0, "y": 0, "contenu" : 1, "dernier_repas" : 0, "age" : -1, "taux_de_croissance" : -1, "capa_de_repro" : 0, 'nb_action' : 0}
case_nourriture = {"x" : 0, "y": 0, "contenu" : 1, "dernier_repas" : 0, "age" : 0, "taux_de_croissance" : -1, "capa_de_repro" : 0, 'nb_action' : 1}
case_vide = {"x" : 0, "y": 0, "contenu" : 0, "dernier_repas" : 0, "age" : 0, "taux_de_croissance" : -1, "capa_de_repro" : 0, 'nb_action' : 1}
case_antibio = {"x" : 0, "y": 0, "contenu" : 2, "dernier_repas" : 0, "age" : 0, "taux_de_croissance" : -1, "capa_de_repro" : 0, 'nb_action' : 1}

###Initialisation des tableaux contenant les données de la boîte en fonction du nombre d'itérations:
nb_vides = []
nb_antibio = []
nb_nourriture = []
nb_bacterie1 = []
nb_bacterie2 = []
nb_total_bacteries =[]

#On définit les correspondances entre les chiffres et leur signification : 0 = vide ; 1 =  nourriture ; 2 = antibiotique ; 3 = bactérie1 ; 4 = bactérie2

from tkinter import *
from tkinter.messagebox import *
import time
import math
import random
import numpy as np
from matplotlib import pyplot as plt

#on définit le type boite par le type list[list[dict[str : Number]]]

###initialisation des paramètres et bacteries

#widget ph_opt, temp_opt, taux de croissance optimal... enfin tous les parametres mis en demande a l'utilisateur pour deux bacteries donc on indice les valeur par le type 1 ou 2 de la bacterie (ex : ph_opt2) sauf pour la temperature de la boite notee temp et son ph note ph qui prennent d'autres curseurs

def taux_de_croissance_effectif(taux_opt, ph, ph_opt, temp, temp_opt):
    """
        float * float * float * int * int -> float
        
        Retourne le taux de croissance effectif de la souche.
    """
    tmin = temp_opt - 20
    tmax = temp_opt + 20
    if temp < tmin or temp > tmax:
        return 0
    a = temp - tmax
    b = (temp - tmin) ** 2
    c = temp_opt - tmin
    d = temp - temp_opt
    e = temp_opt - tmax
    f = temp_opt + tmin - 2*temp
    taux_temp = (a * b) / (c * (c * d - e * f))
    if ph == ph_opt:
        taux_ph = 1
    else:
        ph_min = ph_opt - 3
        ph_max = ph_opt + 3
        if ph < ph_min or ph > ph_max:
            return 0
        a = ph - ph_min
        b = ph - ph_max
        c = ph - ph_opt
        taux_ph = a * b / ( a * b - c**2 )
    return taux_opt * min(1, taux_temp) * min(1, taux_ph)

def init_bact(num_souche, taux_opt, ph, ph_opt, temp, temp_opt):
    """
        int * float * float * float * int * int -> dict[str : Number]
        
        retourne les données de la bactérie sur la case actuelle.
    """
    return {'x' : 0, 'y' : 0, 'contenu' : num_souche + 2,'dernier_repas' : 0, 'age' : 0, 'taux_de_croissance' : taux_de_croissance_effectif(taux_opt, ph, ph_opt, temp, temp_opt), 'capa_de_repro' : 0, 'nb_action' : 0}

###Initialisation de la boite
def coo(x, y):
    """
        int * int -> dict[str : Number]
        
        Initialise la position de la case actuelle. 
    """
    return {'x' : x, 'y' : y, 'contenu' : 1,'dernier_repas' : 0, 'age' : 0, 'taux_de_croissance' : 0, 'capa_de_repro' : 0, 'nb_action' : 0}

def L_dico(k, L):
    """
        int * int -> list[dict[str : Number]]
        
        retourne sous forme de liste une ligne de la boîte
    """
    res = []
    for i in range(0, L):
        res.append(coo(k, i))
    return res

def init_boite(L):
    """
        int -> list[list[dict : Number]]
        
        retourne la boîte initialisée.
    """
    res = []
    for i in range(0,L):
        res.append(L_dico(i, L))
    return res

def pos_alea(boite):
    """
        boite -> tuple[int, int]
        
        retourne des valeurs de position choisies aléatoirement
    """
    L = len(boite);
    l = len(boite[0])
    return (random.choice(range(0, L)), random.choice(range(0, l)))

def init_pos_bact(boite, bact, canvas):
    """
        boite * dict[str : int] * Canvas -> boite
        
        retourne la boite avec les positions de bactéries initialisées.
    """
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
        couleur_souche = "orange"

    canvas.create_rectangle(x0, y0, x1, y1, width = 0, fill = couleur_souche)
    return box

### Trouver le voisinage (à tester avec le dico)(semble marcher quand meme)



def voisinage(boite, x, y, taille) :
    """
        boite * int * int * int -> list[dict[str : Number]]
        
        retourne le voisinage de la case de coordonnées (x, y)
    """
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



### Statistiques
#pas mal de fonctions proches des stats de Schelling

def nb_entites(boite):
    """
        boite -> dict[str : int]
        
        renvoie sous forme de dictionnaire le nombre de bactéries 1 et 2, de cases vides, de nourritures, 
        et d'antibiotique dans la boite lors de la i_ème itération. 
    """
    res = {"Vide" : 0, "Nourriture" : 0, "Antibio" : 0, "Bacterie1" : 0, "Bacterie2" : 0}
    for i in range(0, len(boite)):
        for j in range(0, len(boite[0])):
            contenu = boite[i][j]['contenu']
            if contenu == 0:
                res["Vide"]+=1
            if contenu == 1:
                res["Nourriture"]+=1
            if contenu == 2:
                res["Antibio"]+=1
            if contenu == 3:
                res["Bacterie1"]+=1
            if contenu == 4:
                res["Bacterie2"]+=1
    return res

def affiche_courbes(iter_max, b1, b2, n, a, t_b, v, n_iter):
    """
        int * int * int * int * int * int * int * int -> NoneType
        
        affiche les courbes de la simulation.
    """
    #x = np.linspace(0, iter_max, num=iter_max)
    x = [i for i in range (0, n_iter)]

    plt.plot(x, b1, label = 'souche1', color = 'r')
    plt.plot(x, b2, label = 'souche2', color = 'tab:orange')
    plt.plot(x, n, label = 'nourriture', color ='g')
    plt.plot(x, a, label = 'antibio', color ='b')
    plt.plot(x, t_b, label = 'total_bacteries', color = 'tab:pink')
    plt.plot(x, v, label = 'cases_vides', color = 'k')

    plt.ylabel("Nombre d'entités")
    plt.xlabel("Nombre d'itérations")
    plt.legend()
    plt.show()

###Evolution du système (à changer avec les dico)

def in_liste(contenu, liste): #cherche si un contenu est dans une liste de dico
    """
        int * list[dico[str : int]] -> bool
        
        indique si l'élément demandé est dans une liste ou non.
    """
    for i in range(0, len(liste)):
        if contenu == liste[i]['contenu']:
            return True
    return False

def mort_bacterie(boite, x, y, canvas):
    """
        boite * int * int * Canvas -> boite
        
        fait mourir la bactérie à l'emplacement voulu.
    """
    box = boite
    box[x][y]["x"] = x
    box[x][y]["y"] = y
    box[x][y]["contenu"] = 0
    box[x][y]["dernier_repas"] = 0
    box[x][y]["age"] = 0
    box[x][y]["taux_de_croissance"] = -1
    box[x][y]["capa_de_repro"] = 0
    box[x][y]["nb_action"] = 1
    x0 = str(x) + 'm'
    y0 = str(y) + 'm'
    x1 = str(x + 1) + 'm'
    y1 = str(y + 1) + 'm'
    canvas.create_rectangle(x0, y0, x1, y1, width = 0, fill = "white")
    return box

def mort_antibio(boite, x, y, canvas):
    """
        boite * int * int * Canvas -> boite
        
        Supprime l'antibiotique à l'emplacement voulu.
    """
    box = boite
    box[x][y]["x"] = x
    box[x][y]["y"] = y
    box[x][y]["contenu"] = 0
    box[x][y]["dernier_repas"] = 0
    box[x][y]["age"] = 0
    box[x][y]["taux_de_croissance"] = -1
    box[x][y]["capa_de_repro"] = 0
    box[x][y]["nb_action"] = 1
    x0 = str(x) + 'm'
    y0 = str(y) + 'm'
    x1 = str(x + 1) + 'm'
    y1 = str(y + 1) + 'm'
    canvas.create_rectangle(x0, y0, x1, y1, width = 0, fill = "white")
    return box

def deplacement_possible(boite, x, y):
    """
        boite * int * int -> bool
        
        retourne True si la case sur laquelle la bactérie veut se déplacer est libre, False sinon.
    """
    if boite[x][y]['contenu'] == 3 or boite[x][y]['contenu'] == 4:
        if boite[x][y]['nb_action'] != 0:
            return False
        if len(voisinage_direct_libre(boite, x, y)) > 0:
                return True
    return False


def distance_parcours(x0, y0, x1, y1):
    """
        int * int * int * int -> int
        
        retourne la distance en déplacement entre les case aux coordonnées (x1, y1) et (x2, y2).
    """
    return abs(x1 - x0) + abs(y1 - y0)


def deplacement(boite, x, y, coordonnees, canvas):
    """
        boite * int * int * tuple[int, int]
        
        retourne la boite boite, avec les déplacement de la bactérie effectué.
    """
    new_x, new_y = coordonnees
    box = boite
    if box[new_x][new_y]['contenu'] == 1:
        box[x][y]['dernier_repas'] = 0
    box[new_x][new_y] = box[x][y]
    box[new_x][new_y]['x'] = new_x
    box[new_x][new_y]['y'] = new_y
    box[new_x][new_y]['nb_action'] = 1
    box[x][y] = {"x" : x, "y": y, "contenu" : 0,"dernier_repas" : 0, "age" : 0, "taux_de_croissance" : -1, "capa_de_repro" : 0, 'nb_action' : 1} #laisse un vide après s'être déplacée
    #Afficher le blanc
    x0 = str(x) + 'm'
    y0 = str(y) + 'm'
    x1 = str(x + 1) + 'm'
    y1 = str(y + 1) + 'm'
    canvas.create_rectangle(x0, y0, x1, y1, width = 0, fill = "white")
    #afficher la nouvelle pos
    x0 = str(new_x) + 'm'
    y0 = str(new_y) + 'm'
    x1 = str(new_x + 1) + 'm'
    y1 = str(new_y + 1) + 'm'
    if box[new_x][new_y]['contenu'] == 3:
        canvas.create_rectangle(x0, y0, x1, y1, width = 0, fill = "red")
    if box[new_x][new_y]['contenu'] == 4:
        canvas.create_rectangle(x0, y0, x1, y1, width = 0, fill = "orange")
    return box

def voisinage_direct_libre(boite, x, y):
    """
        boite * int * int -> list[dict[str : Number]]
        
        Retourne les cases adjacentes la bactérie qui sont libres.
    """
    voisinage0 = voisinage(boite, x, y, 1)
    res = []
    contenu = boite[x][y]['contenu']
    for i in range(0, len(voisinage0)):
        case = voisinage0[i]
        if distance_parcours(x, y, case["x"], case['y']) == 1 and (case['contenu'] == 0 or case['contenu'] == 1):
            res.append(case)
        if deux_bact == 1 and distance_parcours(x, y, case["x"], case['y']) == 1 and (case['contenu'] != contenu and ( case['contenu'] == 4 or case["contenu"] == 3 )):
            res.append(case)
    return res

def choix_deplacement(boite, x, y, taille):
    """
        boite * int * int * int -> tuple[int, int]
        
        Retourne la future position de la bactérie.
    """
    if deplacement_possible(boite, x, y):
        box = boite
        voisi = voisinage_direct_libre(box, x ,y)
        choix = voisi[random.choice(range(0, len(voisi)))]
        x = choix["x"]
        y = choix["y"]
        return (x, y)
    else:
        return None

def naissance(boite, x, y, coordonnees, canvas):
    """
        boite * int * int * tuple[int, int] * Canvas -> boite
    
        Retourne la nouvelle boite avec une naissance de bactérie.
    """
    new_x, new_y = coordonnees
    box = boite
    bact_type = box[x][y]['contenu']
    taux = box[x][y]['taux_de_croissance']
    box = deplacement(boite, x, y, coordonnees, canvas)
    box[new_x][new_y]['age'] = 0
    box[x][y]['contenu'] = bact_type
    box[x][y]['dernier_repas'] = 0
    box[x][y]['age'] = 0
    box[x][y]['taux_de_croissance'] = taux
    box[x][y]['capa_de_repro'] = 0
    box[x][y]['nb_action'] = 1
    #affiche la nouvelle bact
    x0 = str(x) + 'm'
    y0 = str(y) + 'm'
    x1 = str(x + 1) + 'm'
    y1 = str(y + 1) + 'm'
    if box[new_x][new_y]['contenu'] == 3:
        canvas.create_rectangle(x0, y0, x1, y1, width = 0, fill = "red")
    if box[new_x][new_y]['contenu'] == 4:
        canvas.create_rectangle(x0, y0, x1, y1, width = 0, fill = "orange")
    return box

def pos_alea_antibio(boite):
    """
        boite -> tuple[int, int]
        
        retourne une position possible pour l'ajout d'antibiotique.
    """
    #la goutte est de hauteur et largeur max 9
    intervalle = range(0,len(boite) - 9)
    x = random.choice(intervalle)
    y = random.choice(intervalle)
    return (x, y)

def remplace_par_antibio_si_non_resis(boite, x, y):
    """
        boite * int * int -> boite
        
        Retourne la boite dans laquelle la bactérie non résistante à l'antibiotique est tuée.
    """
    box = boite
    box[x][y]['contenu'] = 2
    box[x][y]['age'] = 0
    x0 = str(x) + 'm'
    y0 = str(y) + 'm'
    x1 = str(x + 1) + 'm'
    y1 = str(y + 1) + 'm'
    canvas.create_rectangle(x0 , y0, x1, y1, width = 0, fill = "blue")
    return box

def ajout_antibio(boite, coordonnees):
    """
        boite * tuple[int * int] -> boite
        
        Retourne la boite avec l'antibiotique ajouté.
    """
    box = boite
    x, y = coordonnees
    for i in range(-4, 5):
        for j in range(-4, 5):
            if distance_parcours(x, y, x + i, y + j) <= 5 and ( ( (i != -1) or (i != 1) ) and ( (j != -4) or (j != 4) ) ):
                box = remplace_par_antibio_si_non_resis(box, x + i, y + j)
    return box

def coo_vide(boite):
    """
        boite -> list[tuple[int, int]]
        
        Retourne l'ensemble des coordonnees de contenu 0
    """
    res = []
    for i in range(0, len(boite)):
        for j in range(0, len(boite[0])):
            case = boite[i][j]
            if case["contenu"] == 0:
                res.append((case['x'], case['y']))
    return res

def coo_vide_nourriture(boite, demi_cote):
    """
        boite * int -> list[tuple[int, int]]
        
        Retourne l'ensemble des cases avec ajout de nourriture possible
    """
    res = []
    dim = len(boite)
    for i in range(0, len(boite)):
        for j in range(0, len(boite[0])):
            case = boite[i][j]
            if case["contenu"] == 0 and i + demi_cote < dim and i - demi_cote >= 0 and j + demi_cote < dim and j - demi_cote >= 0:
                res.append((case['x'], case['y']))
    return res

def pos_alea_nourriture(boite, demi_cote):
    """
        boite * int -> tuple[int, int]
        
        Retourne la positioin à laquelle on met de la nourriture. 
    """
    liste = coo_vide_nourriture(boite, demi_cote)
    return liste[random.choice(range(0, len(liste)))]

def ajout_nourriture(boite, demi_cote, coordonnees, canvas):
    """
        boite * int * tuple[int, int] * Canvas -> boite
        
        Retourne le nouvelle boite avec la nourriture ajoutée.
    """
    box = boite
    x, y = coordonnees
    for i in range(-demi_cote, demi_cote + 1):
        for j in range(-demi_cote, demi_cote + 1):
            a = x + i
            b = y + j
            case = box[a][b]
            if case["contenu"] == 0:
                box[a][b]["x"] = a
                box[a][b]["y"] = b
                box[a][b]["contenu"] = 1
                box[a][b]["dernier_repas"] = 0
                box[a][b]["age"] = 0
                box[a][b]["taux_de_croissance"] = -1
                box[a][b]["capa_de_repro"] = 0
                box[a][b]["nb_action"] = 1
                x0 = str(a) + 'm'
                y0 = str(b) + 'm'
                x1 = str(a + 1) + 'm'
                y1 = str(b + 1) + 'm'
                canvas.create_rectangle(x0, y0, x1, y1, width = 0, fill = "green")
            if case["contenu"] == 3 or case["contenu"] == 4:
                box[a][b]["dernier_repas"] = 0
    return box

def interact_bact(boite, x, y, coordonnees, canvas):
    """
        boite * int * int * tuple[int, int] * Canvas -> boite
        
        Retourne le boite avec une des bactéries qui est gagnante (dans un duel)
    """
    box = boite
    winner = random.choice(range(0,2))
    new_x, new_y = coordonnees
    if winner == 0:
        box[x][y]["x"] = x
        box[x][y]["y"] = y
        box[x][y]["contenu"] = 0
        box[x][y]["dernier_repas"] = 0
        box[x][y]["age"] = 0
        box[x][y]["taux_de_croissance"] = -1
        box[x][y]["capa_de_repro"] = 0
        box[x][y]["nb_action"] = 1
        x0 = str(x) + 'm'
        y0 = str(y) + 'm'
        x1 = str(x + 1) + 'm'
        y1 = str(y + 1) + 'm'
        canvas.create_rectangle(x0, y0, x1, y1, width = 0, fill = "white")
    else:
        box[new_x][new_y]["x"] = x
        box[new_x][new_y]["y"] = y
        box[new_x][new_y]["contenu"] = 0
        box[new_x][new_y]["dernier_repas"] = 0
        box[new_x][new_y]["age"] = 0
        box[new_x][new_y]["taux_de_croissance"] = -1
        box[new_x][new_y]["capa_de_repro"] = 0
        box[new_x][new_y]["nb_action"] = 1
        x0 = str(new_x) + 'm'
        y0 = str(new_y) + 'm'
        x1 = str(new_x + 1) + 'm'
        y1 = str(new_y + 1) + 'm'
        canvas.create_rectangle(x0, y0, x1, y1, width = 0, fill = "white")
    return box

def evolution_variables(boite):
    """
        boite -> boite
        
        Retourne la boite avec toutes les évolutions liées au variables d'age, de caoacité de reproduction et tue les bactéries qui doivent l'être.
    """
    box = boite

    for i in range(0, len(box)):
        for j in range(0, len(box[0])):
            #augmentation des ages
            contenu = box[i][j]['contenu']
            if contenu >= 2:
                box[i][j]['age']+= 1
                if contenu != 2:
                    box[i][j]['dernier_repas']+= 1
            #vérification des ages et application des morts
            age = box[i][j]['age']
            dernier_repas = box[i][j]['dernier_repas']
            if contenu == 2 and age >= lifespawn_antibio:
                box = mort_antibio(boite, i, j, canvas)
            if contenu == 3 and (age >= lifespawn_bact1 or dernier_repas >= lifespawn_sans_nourriture_bact1):
                box = mort_bacterie(box, i, j, canvas)
            if contenu == 4 and (age >= lifespawn_bact2 or dernier_repas >= lifespawn_sans_nourriture_bact2):
                box = mort_bacterie(box, i, j, canvas)
            #evolution de la capacité de reproduction
            if contenu == 3 or contenu == 4:
                if box[i][j]['capa_de_repro'] < 0.9:
                    box[i][j]['capa_de_repro']+=0.1
            #reset du nombre d'actions
            box[i][j]['nb_action'] = 0

    return box

### Affichage
    
def convert_to_array(boite):
    """
        boite -> array[list[int]]
        
        renvoit la  matrice des contenus de la boite
    """
    res = []
    for i in range(0, len(boite)):
        temp = []
        for j in range(0, len(boite[0])):
            temp.append(boite[i][j]['contenu'])
        res.append(temp)
    return np.array(res)

def plot_boite(boite):
    """
        boite -> NoneType
        
        Affiche la boite avec matplotlib.
    """
    box = boite
    A = convert_to_array(box)
    plt.figure(figsize=(15,12)) # (30,30) = Taille de la figure
    plt.imshow(A,cmap='viridis')
    plt.colorbar()
    plt.tick_params(top=False, bottom=False, right=False, left=False, labelleft=False, labelbottom=False)
    plt.show()


###Global
def continuer(boite):
    """
        boite -> True
        
        Retourne True s'il y a des bactéries
    """
    pop = nb_entites(boite)
    if pop["Bacterie1"] + pop["Bacterie2"] == 0:
        return False
    return True

def tour(boite, canvas):
    """
        boite * Canvas -> boite
        
        Retourne la boite mise à jour
    """
    box = boite
    for i in range(0, len(box)):
        for j in range(0, len(box[0])):
            if deplacement_possible(box, i, j):
                dest = choix_deplacement(box, i, j, 1)
                case = box[i][j]
                new_x, new_y = dest
                if box[new_x][new_y]['contenu'] >= 3:
                    box = interact_bact(box, i, j, dest, canvas)
                if case['age'] > 1 and case['capa_de_repro'] > (1 - case['taux_de_croissance']):
                    box = naissance(box, i, j, dest, canvas)
                else:
                    box = deplacement(box, i, j, dest, canvas)
    box = evolution_variables(box)
    canvas.update()
    return box

def ajout(boite, n_iter, f_antibio, f_nourriture, demi_cote, debut_ajout, canvas):
    """
        boite * int * int * int * int * int * Canvas -> boite
        
        Retourne la boite avec l'antibiotique et la nourriture ajoutée.
    """
    box = boite
    if  f_antibio != 0 and n_iter >= debut_ajout and n_iter % f_antibio == 0:
        box = ajout_antibio(boite, pos_alea_antibio(box))
        #disp.plot_boite(box)
    if  f_nourriture != 0 and n_iter >= debut_ajout and n_iter % f_nourriture == 0 and coo_vide_nourriture(box, demi_cote) != []:
        box = ajout_nourriture(box, demi_cote, pos_alea_nourriture(box, demi_cote), canvas)
        #disp.plot_boite(box)
    return box

def structure_bacterio(iter_max, canvas):
    """
        int * Canvas -> NoneType
        
        Forme la structure du code et retourne None
    """
    res = dict()
    nb_bacterie1 = []
    nb_bacterie2 = []
    nb_nourriture = []
    nb_antibio = []
    nb_total_bacteries = []
    nb_vides = []
    box = init_boite(100)
    box = init_pos_bact(box, init_bact(1, taux1, ph, ph1, temp, temp1), canvas)
    if deux_bact == 1:
        box = init_pos_bact(box, init_bact(2, taux2, ph, ph2, temp, temp2), canvas)
    cmpt = 0
    debut_ajout = 10
    while cmpt <= iter_max and continuer(box):
        box = tour(box, canvas)
        box = ajout(box, cmpt, f_antibio, f_nourriture, demi_cote, debut_ajout, canvas)
        cmpt+=1

        ##On sauvegarde les données de la boîte à la cmpt_ième itération
        res = nb_entites(box)
        nb_bacterie1.append(res["Bacterie1"])
        nb_bacterie2.append(res["Bacterie2"])
        nb_nourriture.append(res["Nourriture"])
        nb_antibio.append(res["Antibio"])
        nb_total_bacteries.append(nb_bacterie1[-1] + nb_bacterie2[-1])
        nb_vides.append(res["Vide"])

    affiche_courbes(iter_max, nb_bacterie1, nb_bacterie2, nb_nourriture, nb_antibio, nb_total_bacteries, nb_vides, cmpt)
    return None

###Fenetre Tkinter

def affichage():
    """
        -> Nonetype
        
        Initialise la fenêtre Tkinter.
    """
    fenetre = Tk()

    label = Label(fenetre, text = "Merci d'utiliser notre simulation de croissance bacteriologique")
    label.pack()
    Label(fenetre, text = "L'unité de température est le degré Celsius.").pack()

    #fenetre['bg']='white'

    # frame 1 parametres bact1
    Frame1 = LabelFrame(fenetre, text="Paramètres sur la première bacterie", padx=20, pady=20)
    Frame1.pack(side = LEFT, fill="both", expand="yes")

    # frame 2 parametre bact2
    Frame2 = LabelFrame(fenetre, text="Paramètres sur la seconde bacterie", padx=20, pady=20)
    Frame2.pack(side = LEFT, fill="both", expand="yes")

    #Frame 4 parametres de la boite
    Frame4 = LabelFrame(fenetre, text = "Paramètres sur la boite", padx = 20, pady = 20)
    Frame4.pack(side = LEFT, fill = "both", expand = "yes")


    # frame 3 boite
    Frame3 = LabelFrame(fenetre, text="Etat de la boite", padx=20, pady=20)
    Frame3.pack(side = RIGHT, fill="both", expand="yes")

    #Frame1
    Label(Frame1, text="Veuillez choisir les paramètres de la premiere bactérie").pack(padx=15, pady = 18)
    taux1_scl = Scale(Frame1, orient='horizontal', from_=0, to=1, resolution=0.1, tickinterval=0.2, length=350, label='Taux de croissance optimal')
    taux1_scl.pack()
    taux1_scl.set(1)

    vie1 = Scale(Frame1, orient='horizontal', from_=0, to=25, resolution=1, tickinterval=5, length=350, label='Durée de vie')
    vie1.pack()
    vie1.set(10)

    vie1_bis = Scale(Frame1, orient='horizontal', from_=0, to=15, resolution=1, tickinterval=5, length=350, label='Durée de vie sans manger')
    vie1_bis.pack()
    vie1_bis.set(5)

    t1 = Scale(Frame1, orient='horizontal', from_=0, to=75, resolution=1, tickinterval=5, length=350, label='Température optimale')
    t1.pack()
    t1.set(25)

    Ph1 = Scale(Frame1, orient='horizontal', from_=3, to=11, resolution=0.5, tickinterval=1, length=350, label='PH optimal')
    Ph1.pack()
    Ph1.set(7.0)

    #Frame 2
    double = IntVar()
    double_chk = Checkbutton(Frame2, text="Deux bacteries ?", variable = double)
    double_chk.pack(pady = 15)


    taux2_scl = Scale(Frame2, orient='horizontal', from_=0, to=1, resolution=0.1, tickinterval=0.2, length=350, label='Taux de croissance optimal')
    taux2_scl.pack()
    taux2_scl.set(1)

    vie2 = Scale(Frame2, orient='horizontal', from_=0, to=25, resolution=1, tickinterval=5, length=350, label='Durée de vie')
    vie2.pack()
    vie2.set(10)

    vie2_bis = Scale(Frame2, orient='horizontal', from_=0, to=15, resolution=1, tickinterval=5, length=350, label='Durée de vie sans manger')
    vie2_bis.pack()
    vie2_bis.set(5)

    t2 = Scale(Frame2, orient='horizontal', from_=0, to=75, resolution=1, tickinterval=5, length=350, label='Température optimale')
    t2.pack()
    t2.set(25)

    Ph2 = Scale(Frame2, orient='horizontal', from_=3, to=11, resolution=0.5, tickinterval=1, length=350, label='PH optimal')
    Ph2.pack()
    Ph2.set(7.0)


    #Frame4
    Label(Frame4, text ="Veuillez choisir les parametres à appliquer sur la boite").pack(padx = 10, pady = 18)

    t = Scale(Frame4, orient='horizontal', from_=0, to=75, resolution=1, tickinterval=5, length=350, label='Température de la boite')
    t.pack()
    t.set(25)

    Ph = Scale(Frame4, orient='horizontal', from_=3, to=11, resolution=0.5, tickinterval=1, length=350, label='PH de la boite')
    Ph.pack()
    Ph.set(7.0)

    nour = Scale(Frame4, orient='horizontal', from_=0, to=50, resolution=5, tickinterval=5, length=350, label="Ajout de nourriture tous les X tours (0 = pas d'ajout)")
    nour.pack()
    nour.set(30)

    Qnour = Scale(Frame4, orient='horizontal', from_=0, to=10, resolution=1, tickinterval=2, length=350, label='Quantité de nourriture')
    Qnour.pack()
    Qnour.set(5)

    antib = Scale(Frame4, orient = 'horizontal', from_ = 0, to = 50, resolution=5, tickinterval=10, length=350, label="Ajout d'antibiotique tous les X tours (0 = pas d'ajout)")
    antib.pack()
    antib.set(20)

    vie_antib = Scale(Frame4, orient ="horizontal", from_= 0, to = 50, resolution = 5, tickinterval = 10, length=350, label ="Durée de 'vie' de l'antibiotique")
    vie_antib.pack()
    vie_antib.set(20)

    Label(Frame4, text = "Nombre maximal d'itérations").pack()
    iter = StringVar()
    iter_ent = Entry(Frame4, textvariable = iter)
    iter_ent.pack()
    iter.set("20")

    #Frame3
    canvas0 = Canvas(Frame3, width="99m", height="99m", background='black')
    canvas0.pack()
    canvas = init_canvas(canvas0)
    globals()["canvas0"] = canvas0
    globals()["canvas"] = canvas
    
    Label(Frame3, text="L'optimisation n'étant pas exceptionnelle,\n le temps de calcul peut être long pour des grands nombres d'itérations").pack(pady = 50)

    #Boutons pour lancer la simulation
    globall(taux1_scl, taux2_scl, vie1, vie2, vie1_bis, vie2_bis, vie_antib, t1, t2, Ph1, Ph2, double, double_chk, t, Ph, nour, Qnour, antib, iter, iter_ent)

    #recup_valeur = Button(Frame1, text="Récupère les valeurs inscrites", command = getall)
    #recup_valeur.pack(side = "bottom")

    launcher = Button(Frame2, text="Lancer la simulation", command = lancer)
    launcher.pack(side="bottom")

    reseteur = Button(Frame3, text ="Reset boite", command = reset)
    reseteur.pack(side = "bottom")

    fenetre.mainloop()
    return None

def reset():
    """
        ->NonteType
        
        Réinitialise le canvas et retourne None
    """
    globals()["canvas"] = init_canvas(canvas0)
    return None

def lancer():
    """
        ->NoneType
        
        Lance la simulation et retourne None.
    """
    getall()
    if type(iter_max) == int and iter_max > 0:
        structure_bacterio(iter_max, canvas)
    else:
        showerror("Erreur", "Veuillez vérifier les saisies,\n le nombre d'itération doit être un entier strictement positif")
    return None


def globall(taux1, taux2, vie1, vie2, vie1_bis, vie2_bis, vie_antib, t1, t2, Ph1, Ph2, double, double_chk, t, Ph, nour, Qnour, antib, iter, iter_ent):
    """
        float*18 * int * int -> NoneType
        
        Retourne None après avoir initialisé les variables globales.
    """
    globals()["taux1_scl"] = taux1
    globals()["taux2_scl"] = taux2
    globals()["vie1"] = vie1
    globals()["vie2"] = vie2
    globals()["vie1_bis"] = vie1_bis
    globals()["vie2_bis"] = vie2_bis
    globals()["vie_antib"] = vie_antib
    globals()["t1"] = t1
    globals()["t2"] = t2
    globals()["Ph1"] = Ph1
    globals()["Ph2"] = Ph2
    globals()["double"] = double
    globals()["double_chk"] = double_chk
    globals()["t"] = t
    globals()["Ph"] = Ph
    globals()["nour"] = nour
    globals()["Qnour"] = Qnour
    globals()["antib"] = antib
    globals()["iter"] = iter
    globals()["iter_ent"] = iter_ent
    return None

def getall():
    """
        -> NoneType
        
        Récupère les valeurs des curseurs et les attribue aux variables globales correspondante
    """
    globals()["taux1"] = taux1_scl.get()
    globals()["taux2"] = taux2_scl.get()
    globals()["lifespawn_bact1"] = vie1.get()
    globals()["lifespawn_bact2"] = vie2.get()
    globals()["lifespawn_sans_nourriture_bact1"] = vie1_bis.get()
    globals()["lifespawn_sans_nourriture_bact2"] = vie2_bis.get()
    globals()["lifespawn_antibio"] = vie_antib.get()
    globals()["temp1"] = t1.get()
    globals()["temp2"] = t2.get()
    globals()["ph1"] = Ph1.get()
    globals()["ph2"] = Ph2.get()
    globals()["deux_bact"] = double.get() #Renvoie 1 si cochée 0 sinon
    globals()["temp"] = t.get()
    globals()["ph"] = Ph.get()
    globals()["f_nourriture"] = nour.get()
    globals()["demi_cote"] = Qnour.get()
    globals()["f_antibio"] = antib.get()
    globals()["iter_max"] = int(iter.get())
    return None


def init_canvas(canvas):
    """
        Canvas -> Canvas
        
        Retourne un Canvas initialisé.
    """
    #ls = []
    for i in range(0, 100):
        for j in range(0, 100):
            x0 = str(i) + 'm'
            y0 = str(j) + 'm'
            x1 = str(i + 1) + 'm'
            y1 = str(j + 1) + 'm'
            temp = canvas.create_rectangle(x0, y0, x1, y1, width = "0m", fill = "green")
            #ls.append(temp)
    return canvas



affichage()
