lt = 5
Lt = 5
test = [[1, 1, ,1 ,1 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]

#On définit les correspondances entre les chiffres et leur signification : 0 = vide ; 1 =  nourriture ; 2 = antibiotique ; 3 = bactérie1 ; 4 = bactérie2

def init_boite(l, L):
    res = [l * [0]] * L
    return res

def voisinage(boite, x, y, taille) :
    res = []
    if rue + neigh_spatial < len(world) and rue - neigh_spatial >= 0:
        if num_rue - neigh_spatial >= 0 and num_rue + neigh_spatial < len(world[0]):
            for i in range(-neigh_spatial, neigh_spatial + 1):
                for j in range(- neigh_spatial, neigh_spatial + 1):
                    if i == 0:
                        if j != 0:
                            res.append(world[rue + i][num_rue + j])
                    else:
                        res.append(world[rue + i][num_rue + j])
        if num_rue - neigh_spatial < 0:
            for i in range(-neigh_spatial, neigh_spatial + 1):
                for j in range(0, neigh_spatial + 1):
                    if i == 0:
                        if j != 0:
                            res.append(world[rue + i][num_rue + j])
                    else:
                        res.append(world[rue + i][num_rue + j])
        if num_rue + neigh_spatial >= len(world[0]):
            for i in range(-neigh_spatial, neigh_spatial + 1):
                for j in range(- neigh_spatial, 1):
                    if i == 0:
                        if j != 0:
                            res.append(world[rue + i][num_rue + j])
                    else:
                        res.append(world[rue + i][num_rue + j])

    if rue + neigh_spatial >= len(world) and rue - neigh_spatial >= 0:
        if num_rue - neigh_spatial >= 0 and num_rue + neigh_spatial < len(world[0]):
            for i in range(-neigh_spatial, 1):
                for j in range(- neigh_spatial, neigh_spatial + 1):
                    if i == 0:
                        if j != 0:
                            res.append(world[rue + i][num_rue + j])
                    else:
                        res.append(world[rue + i][num_rue + j])
        if num_rue - neigh_spatial < 0:
            for i in range(-neigh_spatial, 1):
                for j in range(0, neigh_spatial + 1):
                    if i == 0:
                        if j != 0:
                            res.append(world[rue + i][num_rue + j])
                    else:
                        res.append(world[rue + i][num_rue + j])
        if num_rue + neigh_spatial >= len(world[0]):
            for i in range(-neigh_spatial, 1):
                for j in range(- neigh_spatial, 1):
                    if i == 0:
                        if j != 0:
                            res.append(world[rue + i][num_rue + j])
                    else:
                        res.append(world[rue + i][num_rue + j])

    if rue + neigh_spatial < len(world) and rue - neigh_spatial < 0:
        if num_rue - neigh_spatial >= 0 and num_rue + neigh_spatial < len(world[0]):
            for i in range(0, neigh_spatial + 1):
                for j in range(- neigh_spatial, neigh_spatial + 1):
                    if i == 0:
                        if j != 0:
                            res.append(world[rue + i][num_rue + j])
                    else:
                        res.append(world[rue + i][num_rue + j])
        if num_rue - neigh_spatial < 0:
            for i in range(0, neigh_spatial + 1):
                for j in range(0, neigh_spatial + 1):
                    if i == 0:
                        if j != 0:
                            res.append(world[rue + i][num_rue + j])
                    else:
                        res.append(world[rue + i][num_rue + j])
        if num_rue + neigh_spatial >= len(world[0]):
            for i in range(0, neigh_spatial + 1):
                for j in range(- neigh_spatial, 1):
                    if i == 0:
                        if j != 0:
                            res.append(world[rue + i][num_rue + j])
                    else:
                        res.append(world[rue + i][num_rue + j])
    return res