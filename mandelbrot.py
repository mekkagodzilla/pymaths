
from math import sqrt

u = [1, 2]
v = [3, 4]


def cAdd(a, b):
    '''Additionne deux nombres complexes, a et b'''
    return [a[0]+b[0], a[1]+b[1]] 


def cMult(n, m):
    '''Multiplie deux complexes n et m'''
    '''
    (a + bi)·(c + di)
    = ac + adi + bic + bdi²
    = ac + (ad + bc)·i + bd·(-1)
    = ac - bd + (ad + bc)·i
    = partie réelle, partie imaginaire
    '''
    realPart = n[0]*m[0] - n[1] * m[1]
    iPart = n[0]*m[1] + n[1]*m[0]
    return [realPart, iPart]

def magnitude(z):
    return sqrt(z[0]**2 + z[1]**2)


def mandelbrot(z, num):
    '''Exécute num fois le processus et retourne le nombre de divergences'''
    count = 0
    # Définit z1 en z
    z1 = z
    # Réitère num fois:
    while count <= num:
        #vérifie la divergence
        if magnitude(z1) > 2.0:
            # retourne le nombre d'itérations nécessaires pour diverger
            return count
        # Calcule le prochain z
        z1 = cAdd(cMult(z1,z1), z)
        count += 1
    # si au bout du compte z n'a pas divergé après num itération
    return num

# intervalle des valeurs en x:
xmin = -2
xmax = 2

# intervalle des valeurs de y

ymin = -2
ymax = 2

# calcul la longueur de l'intervalle

rangex = xmax - xmin
rangey = ymax - ymin

def setup():
    global xscl, yscl
    size(600,600)
    noStroke()
    xscl = float(rangex)/width
    yscl = float(rangey)/height

def draw():
    # l'origine au centre
    translate(width/2, height/2)
    # parcourt les x et y de la grille
    for x in range(width):
        for y in range(height):
            z = [(xmin + x * xscl), (ymin + y * yscl)]
            # les donne à la fonction mandelbrot()
            col = mandelbrot(z, 100)
            #si mandelbrot() retourne 0
            if col == 100:
                fill(0) # rend le rectangle noir
            else:
                fill(255) # rend le rectangle blan
            #trace un petit rectangle
            rect(x,y,1,1)