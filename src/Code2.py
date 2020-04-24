#NE JAMAIS UTILISER CES DICO POUR REMPLACER LE CONTENU D'UNE CASE ! JAMAIS
dict_ex = {"souche" : 0, "x" : 0, "y": 0, "contenu" : 1, "dernier_repas" : 0, "age" : -1, "resistance" : -1, "taux_de_croissance" : -1, "capa_de_repro" : 0, 'nb_action' : 0}
case_nourriture = {"souche" : 0, "x" : 0, "y": 0, "contenu" : 1, "dernier_repas" : 0, "age" : 0, "resistance" : -1, "taux_de_croissance" : -1, "capa_de_repro" : 0, 'nb_action' : 1}
case_vide = {"souche" : 0, "x" : 0, "y": 0, "contenu" : 0, "dernier_repas" : 0, "age" : 0, "resistance" : -1, "taux_de_croissance" : -1, "capa_de_repro" : 0, 'nb_action' : 1}
case_antibio = {"souche" : 0, "x" : 0, "y": 0, "contenu" : 2, "dernier_repas" : 0, "age" : 0, "resistance" : -1, "taux_de_croissance" : -1, "capa_de_repro" : 0, 'nb_action' : 1}

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
import inits as ins
import displays as disp
import stats

def pause0():
    programPause = input("Press the <ENTER> key to continue...")

###Paramètres globaux à modifier avec les curseurs

"""lifespawn_bact1 = 20
lifespawn_bact2 = 1
lifespawn_sans_nourriture_bact1 = 20
lifespawn_sans_nourriture_bact2 = 5
lifespawn_antibio = 20
temp1 = 25
temp2 = 25
ph1 = 7
ph2 = 7
deux_bact = 0
symbiose = 0
temp = 25
ph = 7
f_nourriture = 20
quantite = 0
f_antibio = 20
iter_max = 100"""

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

def mort_bacterie(boite, x, y, canvas):
    box = boite
    box[x][y] = {"x" : x, "y": y, "contenu" : 0, 'dernier_repas' : 0, "age" : 0, "resistance" : -1, "taux_de_croissance" : -1, 'capa_de_repro' : 0, 'nb_action' : 1}
    x0 = str(x) + 'm'
    y0 = str(y) + 'm'
    x1 = str(x + 1) + 'm'
    y1 = str(y + 1) + 'm'
    canvas.create_rectangle(x0, y0, x1, y1, width = 0, fill = "white")
    return box

def mort_antibio(boite, x, y, canvas):
    box = boite
    box[x][y] = {"x" : x, "y": y, "contenu" : 0, 'dernier_repas' : 0, "age" : 0, "resistance" : -1, "taux_de_croissance" : -1, 'capa_de_repro' : 0, 'nb_action' : 1}
    x0 = str(x) + 'm'
    y0 = str(y) + 'm'
    x1 = str(x + 1) + 'm'
    y1 = str(y + 1) + 'm'
    canvas.create_rectangle(x0, y0, x1, y1, width = 0, fill = "white")
    return box

def deplacement_possible(boite, x, y):
    if boite[x][y]['contenu'] == 3 or boite[x][y]['contenu'] == 4:
        if boite[x][y]['nb_action'] != 0:
            return False
        if len(voisinage_direct_libre(boite, x, y)) > 0:
                return True
    return False

def distance(x0, y0, x1, y1):
    return math.sqrt((x1 - x0)**2 + (y1 - y0)**2)

def distance_parcours(x0, y0, x1, y1):
    return abs(x1 - x0) + abs(y1 - y0)

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

def deplacement(boite, x, y, coordonnees, canvas):
    new_x, new_y = coordonnees
    box = boite
    if box[new_x][new_y]['contenu'] == 1:
        box[x][y]['dernier_repas'] = 0
    box[new_x][new_y] = box[x][y]
    box[new_x][new_y]['x'] = new_x
    box[new_x][new_y]['y'] = new_y
    box[new_x][new_y]['nb_action'] = 1
    box[x][y] = {"x" : x, "y": y, "contenu" : 0,"dernier_repas" : 0, "age" : 0, "resistance" : -1, "taux_de_croissance" : -1, "capa_de_repro" : 0, 'nb_action' : 1} #laisse un vide après s'être déplacée
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
    canvas.create_rectangle(x0, y0, x1, y1, width = 0, fill = "red")
    return box

def voisinage_direct_libre(boite, x, y):
    voisinage0 = voisinage(boite, x, y, 1)
    res = []
    for i in range(0, len(voisinage0)):
        case = voisinage0[i]
        if mn.distance_parcours(x, y, case["x"], case['y']) == 1 and ( (case['contenu'] == 0 or case['contenu'] == 1) or (boite[x][y]['resistance'] != -1 and case['contenu'] == 2) ):
            res.append(case)
    return res

def choix_deplacement(boite, x, y, taille):
    if mn.deplacement_possible(boite, x, y):
        box = boite
        voisi = voisinage_direct_libre(box, x ,y)
        choix = voisi[random.choice(range(0, len(voisi)))]
        x = choix["x"]
        y = choix["y"]
        return (x, y)
    else:
        return None

def naissance(boite, x, y, coordonnees, canvas):
    new_x, new_y = coordonnees
    box = boite
    bact_type = box[x][y]['contenu']
    resi = box[x][y]['resistance']
    taux = box[x][y]['taux_de_croissance']
    box = deplacement(boite, x, y, coordonnees, canvas)
    box[x][y]['contenu'] = bact_type
    box[x][y]['dernier_repas'] = 0
    box[x][y]['age'] = 0
    box[x][y]['resistance'] = resi
    box[x][y]['taux_de_croissance'] = taux
    box[x][y]['capa_de_repro'] = 0
    box[x][y]['nb_action'] = 1
    #affiche la nouvelle bact
    x0 = str(x) + 'm'
    y0 = str(y) + 'm'
    x1 = str(x + 1) + 'm'
    y1 = str(y + 1) + 'm'
    canvas.create_rectangle(x0, y0, x1, y1, width = 0, fill = "red")
    """#afficher la nouvelle pos
    x0 = str(new_x) + 'm'
    y0 = str(new_y) + 'm'
    x1 = str(new_x + 1) + 'm'
    y1 = str(new_y + 1) + 'm'
    canvas.create_rectangle(x0, y0, x1, y1, width = 0, fill = "red")"""
    return box

def pos_alea_antibio(boite):
    #la goutte est de hauteur et largeur max 9
    intervalle = range(0,len(boite) - 9)
    x = random.choice(intervalle)
    y = random.choice(intervalle)
    return (x, y)

def remplace_par_antibio_si_non_resis(boite, x, y):
    box = boite
    if box[x][y]['resistance'] == -1:
        box[x][y]['contenu'] = 2
        box[x][y]['age'] = 0
    return box

def ajout_antibio(boite, coordonnees, canvas):
    """je suppose qu'on prend 100 * 100 en format de boite pour faire l'echelle de la goute"""
    box = boite
    x, y = coordonnees
    for i in range(-4, 5):
        for j in range(-4, 5):
            if distance_parcours(x, y, x + i, y + j) <= 5 and ( ( (i != -1) or (i != 1) ) and ( (j != -4) or (j != 4) ) ):
                box = remplace_par_antibio_si_non_resis(box, x + i, y + j)
                x0 = str(i) + 'm'
                y0 = str(j) + 'm'
                x1 = str(i + 1) + 'm'
                y1 = str(j + 1) + 'm'
                canvas.create_rectangle(x0 , y0, x1, y1, width = 0, fill = "blue")
    return box

def evo_age(boite):
    box = boite
    for i in range(0, len(box)):
        for j in range(0, len(box[0])):
            contenu = box[i][j]['contenu']
            if contenu >= 2:
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

def death_verif_and_apply(boite, canvas):
    box = boite
    for i in range(0, len(box)):
        for j in range(0, len(box[0])):
            contenu = box[i][j]['contenu']
            age = box[i][j]['age']
            dernier_repas = box[i][j]['dernier_repas']
            if contenu == 2 and age >= lifespawn_antibio:
                mort_antibio(boite, i, j, canvas)
            if contenu == 3 and (age >= lifespawn_bact1 or dernier_repas >= lifespawn_sans_nourriture_bact1):
                box = mort_bacterie(box, i, j, canvas)
            if contenu == 4 and (age >= lifespawn_bact2 or dernier_repas >= lifespawn_sans_nourriture_bact2):
                box = mort_bacterie(box, i, j, canvas)
    return box

def reset_nb_action(boite):
    box = boite
    for i in range(0, len(box)):
        for j in range(0, len(box[0])):
            box[i][j]['nb_action'] = 0
    return box

def coo_vide(boite):
    """determine l'ensemble des coordonnees de contenu 0"""
    res = []
    for i in range(0, len(boite)):
        for j in range(0, len(boite[0])):
            case = boite[i][j]
            if case["contenu"] == 0:
                res.append((case['x'], case['y']))
    return res

def coo_vide_nourriture(boite, demi_cote):
    """dertermine l'ensemble des cases avec ajout de nourriture possible"""
    res = []
    dim = len(boite)
    for i in range(0, len(boite)):
        for j in range(0, len(boite[0])):
            case = boite[i][j]
            if case["contenu"] == 0 and i + demi_cote < dim and i - demi_cote >= 0 and j + demi_cote < dim and j - demi_cote >= 0:
                res.append((case['x'], case['y']))
    return res

def pos_alea_nourriture(boite, demi_cote):
    liste = coo_vide_nourriture(boite, demi_cote)
    return liste[random.choice(range(0, len(liste)))]

def ajout_nourriture(boite, demi_cote, coordonnees, canvas):
    box = boite
    x, y = coordonnees
    for i in range(-demi_cote, demi_cote + 1):
        for j in range(-demi_cote, demi_cote + 1):
            a = x + i
            b = y + j
            case = box[a][b]
            if case["contenu"] == 0:
                box[a][b] = {"x" : a, "y": b, "contenu" : 1, "dernier_repas" : 0, "age" : 0, "resistance" : -1, "taux_de_croissance" : -1, "capa_de_repro" : 0, 'nb_action' : 1}
                x0 = str(a) + 'm'
                y0 = str(b) + 'm'
                x1 = str(a + 1) + 'm'
                y1 = str(b + 1) + 'm'
                canvas.create_rectangle(x0, y0, x1, y1, width = 0, fill = "green")
    return box

###Global
def continuer(boite):
    pop = nombre_individus(boite)
    if pop["Bacterie1"] + pop["Bacterie2"] == 0:
        return False
    return True

def tour(boite, canvas):
    box = boite
    for i in range(0, len(box)):
        for j in range(0, len(box[0])):
            if deplacement_possible(box, i, j):
                dest = choix_deplacement(box, i, j, 1)
                case = box[i][j]
                if case['age'] >= 1 and case['capa_de_repro'] >= (1 - case['taux_de_croissance']):
                    box = naissance(box, i, j, dest, canvas)
                else:
                    box = deplacement(box, i, j, dest, canvas)
    box = evo_age(box)
    box = death_verif_and_apply(box, canvas)
    box = evo_capa_de_reprod(box)
    box = reset_nb_action(box)
    return box

def ajout(boite, n_iter, f_antibio, f_nourriture, demi_cote, debut_ajout, canvas):
    box = boite
    if  f_antibio != 0 and n_iter >= debut_ajout and n_iter % f_antibio == 0:
        box = mn.ajout_antibio(boite, pos_alea_antibio(box), canvas)
    if  f_nourriture != 0 and n_iter >= debut_ajout and n_iter % f_nourriture == 0 and coo_vide_nourriture(box, demi_cote) != []:
        box = mn.ajout_nourriture(box, demi_cote, pos_alea_nourriture(box, demi_cote), canvas)
        #plot_boite(box)
    return box

def structure_bacterio(iter_max, canvas):
    res_bac = dict()
    res_autres = dict()
    """temp = 25
    ph = 7
    f_antibio = 25
    f_nourriture = 20
    demi_cote = 5"""
    box = ins.init_boite(10)
    ins.init_pos_bact(box, ins.init_bact(1, 1, ph, 8, temp, 30), canvas)
    cmpt = 0
    debut_ajout = 10
    while cmpt < iter_max and continuer(box):
        box = tour(box, canvas)
        box = ajout(box, cmpt, f_antibio, f_nourriture, demi_cote, debut_ajout, canvas)
        cmpt+=1

        ##On sauvegarde les données de la boîte à la cmpt_ième itération
        res_bac = stats.nombre_individus(box)
        res_autres = stats.nombre_nourriture_antibio(box)
        nb_bacterie1.append(res_bac["Bacterie1"])
        nb_bacterie2.append(res_bac["Bacterie2"])
        nb_nourriture.append(res_autres["Nourriture"])
        nb_antibio.append(res_autres["Antibio"])
        nb_total_bacteries.append(nb_bacterie1[-1] + nb_bacterie2[-1])
        nb_vides.append(res_autres["Vide"])

        #bouge_canvas(box, canvas)
        #canvas.pack()
        disp.plot_boite(box)
    stats.affiche_courbes(iter_max, nb_bacterie1, nb_bacterie2, nb_nourriture, nb_antibio, nb_total_bacteries, nb_vides)
    return None

###Fenetre Tkinter

def affichage():

    fenetre = Tk()

    label = Label(fenetre, text = "Merci d'utiliser notre simulation de croissance bacteriologique")
    label.pack()

    #fenetre['bg']='white'

    # frame 1 parametres bact1
    Frame1 = LabelFrame(fenetre, text="Parametres sur la premiere bacterie", padx=20, pady=20)
    Frame1.pack(side = LEFT, fill="both", expand="yes")

    # frame 2 parametre bact2
    Frame2 = LabelFrame(fenetre, text="Parametres sur la seconde bacterie", padx=20, pady=20)
    Frame2.pack(side = LEFT, fill="both", expand="yes")

    #Frame 4 parametres de la boite
    Frame4 = LabelFrame(fenetre, text = "Parametres sur la boite", padx = 20, pady = 20)
    Frame4.pack(side = LEFT, fill = "both", expand = "yes")


    # frame 3 boite
    Frame3 = LabelFrame(fenetre, text="Etat de la boite", padx=20, pady=20)
    Frame3.pack(side = RIGHT, fill="both", expand="yes")

    """Ajout de labels
    Label(Frame1, text="Parametre sur la premiere bacterie").pack(padx=10, pady=10)
    Label(Frame2, text="Parametre sur la seconde bacterie").pack(padx=10, pady=10)
    Label(Frame3, text="Etat de la boite").pack(padx=10, pady=10)"""

    #Frame1
    Label(Frame1, text="Veuillez choisir les paramètres de la premiere bactérie").pack(padx=15, pady = 18)
    taux1 = Scale(Frame1, orient='horizontal', from_=0, to=1, resolution=0.1, tickinterval=0.2, length=350, label='Taux de croissance optimal')
    taux1.pack()
    taux1.set(0.5)

    vie1 = Scale(Frame1, orient='horizontal', from_=0, to=50, resolution=1, tickinterval=5, length=350, label='Durée de vie')
    vie1.pack()
    vie1.set(25)

    vie1_bis = Scale(Frame1, orient='horizontal', from_=0, to=50, resolution=1, tickinterval=5, length=350, label='Durée de vie sans manger')
    vie1_bis.pack()
    vie1_bis.set(25)

    t1 = Scale(Frame1, orient='horizontal', from_=0, to=75, resolution=1, tickinterval=5, length=350, label='Température optimale')
    t1.pack()
    t1.set(25)

    Ph1 = Scale(Frame1, orient='horizontal', from_=1, to=11.5, resolution=0.5, tickinterval=1, length=350, label='PH optimal')
    Ph1.pack()
    Ph1.set(7.0)

    #Frame 2
    double = IntVar()
    double_chk = Checkbutton(Frame2, text="Deux bacteries ?", variable = double)
    double_chk.pack()

    symb = IntVar()
    symb_chk = Checkbutton(Frame2, text = "Symbiose ?", variable = symb)
    symb_chk.pack(padx = 0, pady = 0)

    taux2 = Scale(Frame2, orient='horizontal', from_=0, to=1, resolution=0.1, tickinterval=0.2, length=350, label='Taux de croissance optimal')
    taux2.pack()
    taux2.set(0.5)

    vie2 = Scale(Frame2, orient='horizontal', from_=0, to=50, resolution=1, tickinterval=5, length=350, label='Durée de vie')
    vie2.pack()
    vie2.set(25)

    vie2_bis = Scale(Frame2, orient='horizontal', from_=0, to=50, resolution=1, tickinterval=5, length=350, label='Durée de vie sans manger')
    vie2_bis.pack()
    vie2_bis.set(25)

    t2 = Scale(Frame2, orient='horizontal', from_=0, to=75, resolution=1, tickinterval=5, length=350, label='Température optimale')
    t2.pack()
    t2.set(25)

    Ph2 = Scale(Frame2, orient='horizontal', from_=1, to=11.5, resolution=0.5, tickinterval=1, length=350, label='PH optimal')
    Ph2.pack()
    Ph2.set(7.0)


    #Frame4
    Label(Frame4, text ="Veuillez choisir les parametres à appliquer sur la boite").pack(padx = 10, pady = 18)

    t = Scale(Frame4, orient='horizontal', from_=0, to=75, resolution=1, tickinterval=5, length=350, label='Température de la boite')
    t.pack()
    t.set(25)

    Ph = Scale(Frame4, orient='horizontal', from_=1, to=11.5, resolution=0.5, tickinterval=1, length=350, label='PH de la boite')
    Ph.pack()
    Ph.set(7.0)

    nour = Scale(Frame4, orient='horizontal', from_=0, to=100, resolution=5, tickinterval=10, length=350, label="Ajout de nourriture tous les X tours (0 = pas d'ajout)")
    nour.pack()
    nour.set(30)

    Qnour = Scale(Frame4, orient='horizontal', from_=1, to=20, resolution=1, tickinterval=2, length=350, label='Quantité de nourriture')
    Qnour.pack()
    Qnour.set(15)

    antib = Scale(Frame4, orient = 'horizontal', from_ = 0, to = 100, resolution=5, tickinterval=10, length=350, label="Ajout d'antibiotique tous les X tours (0 = pas d'ajout)")
    antib.pack()
    antib.set(35)

    vie_antib = Scale(Frame4, orient ="horizontal", from_= 0, to = 100, resolution = 5, tickinterval = 10, length=350, label ="Durée de 'vie' de l'antibiotique")
    vie_antib.pack()
    vie_antib.set(20)

    Label(Frame4, text = "Nombre maximal d'itérations").pack()
    iter = StringVar()
    iter_ent = Entry(Frame4, textvariable = iter)
    iter_ent.pack()
    iter.set("20")

    #Frame3
    canvas = Canvas(Frame3, width="99m", height="99m", background='black')
    canvas.pack()
    canvas = init_canvas(canvas)
    globals()["canvas"] = canvas

    #Boutons pour lancer la simulation
    globall(vie1, vie2, vie1_bis, vie2_bis, vie_antib, t1, t2, Ph1, Ph2, double, double_chk, symb, symb_chk, t, Ph, nour, Qnour, antib, iter, iter_ent)

    recup_valeur = Button(Frame1, text="Récupère les valeurs inscrites", command = getall)
    recup_valeur.pack(side = "bottom")

    launcher = Button(Frame2, text="Lancer la simulation", command = lancer)
    launcher.pack(side="bottom")

    reseteur = Button(Frame3, text ="Reset boite", command = reset)
    reseteur.pack(side = "bottom")

    fenetre.mainloop()
    return None

def reset():
    init_canvas(canvas)
    return None

def lancer():
    if type(iter_max) == int and iter_max > 0:
        structure_bacterio(iter_max, canvas)
    else:
        showerror("Erreur", "Veuillez vérifier les saisies et recliquer sur le bouton en bas à gauche de la fenêtre")
    return None


def globall(vie1, vie2, vie1_bis, vie2_bis, vie_antib, t1, t2, Ph1, Ph2, double, double_chk, symb, symb_chk, t, Ph, nour, Qnour, antib, iter, iter_ent):
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
    globals()["symb"] = symb
    globals()["symb_chk"] = symb_chk
    globals()["t"] = t
    globals()["Ph"] = Ph
    globals()["nour"] = nour
    globals()["Qnour"] = Qnour
    globals()["antib"] = antib
    globals()["iter"] = iter
    globals()["iter_ent"] = iter_ent
    return None

def getall():
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
    globals()["symbiose"] = symb.get() #Renvoie 1 si cochée 0 sinon
    globals()["temp"] = t.get()
    globals()["ph"] = Ph.get()
    globals()["f_nourriture"] = nour.get()
    globals()["demi_cote"] = Qnour.get()
    globals()["f_antibio"] = antib.get()
    globals()["iter_max"] = int(iter.get())
    return None


def init_canvas(canvas):
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

def bouge_canvas(box, canvas):
    arr = convert_to_array(box)
    for i in range(0, len(arr)):
        for j in range(0, len(arr[0])):
            contenu = arr[i][j]
            if contenu == 0:
                canvas.create_rectangle(i, j, i + 1, j + 1, width = 0, fill = "white")
            if contenu == 1:
                canvas.create_rectangle(i, j, i + 1, j + 1, width = 0, fill = "green")
            if contenu == 2:
                canvas.create_rectangle(i, j, i + 1, j + 1, width = 0, fill = "blue")
            if contenu == 3:
                canvas.create_rectangle(i, j, i + 1, j + 1, width = 0, fill = "red")
            if contenu == 4:
                canvas.create_rectangle(i, j, i + 1, j + 1, width = 0, fill = "orange")