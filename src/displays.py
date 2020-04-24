from tkinter import *
from tkinter.messagebox import *
import time
import math
import random
import numpy as np
from matplotlib import pyplot as plt
import inits as ins
import stats

### Affichage
def convert_to_array(boite):
    res = []
    for i in range(0, len(boite)):
        temp = []
        for j in range(0, len(boite[0])):
            temp.append(boite[i][j]['contenu'])
        res.append(temp)
    return np.array(res)

"""def convert_for_tkinter(boite):
    res = []
    for i in range(0, 49):"""

def plot_boite(boite):
    box = boite
    A = convert_to_array(box)
    plt.figure(figsize=(15,12)) # (30,30) = Taille de la figure
    plt.imshow(A,cmap='viridis')
    plt.colorbar()
    plt.tick_params(top=False, bottom=False, right=False, left=False, labelleft=False, labelbottom=False)
    plt.show()