# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 01:56:54 2020

@author: afama
"""

def testAjMod():#juste pour le développement, savoir si l'ajout du module a fonctionné ou non (sous frome de printf)
    print("L'ajout du module a fonctionné")
    
class Bacterie:
    def __init__(self):
        self.souche = 0 #Attribue le type (ou souche) de la bactérie (1 ou 2)
        self.symb = 0 #Indique si la bactérie agit en Symbiose ou en Compétition
        self.x = 0 #indique la coordonnée x de la bactérie dans la boîte de pétri
        self.y = 0 #coordonnée y
        self.age = 0 
        self.resistance = 0
        self.taux_de_croissance = 0
        