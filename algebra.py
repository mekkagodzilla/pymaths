from math import sqrt

def g(x):
    return 6*x**3 + 31*x**2 + 3*x -10


def plug():
    x = -100
    while x < 100:
        print("Trying", x)
        if g(x) == 0:
            print("x = ", x)
            break
        x += 1
    print("done.")

plug()

def equation(a, b, c, d):
    """solves first degree equations of the form ax +b = cx + d"""
    return (d - b)/(a - c)

def quad(a, b, c):
    x1 = (-b+sqrt(b**2 - 4*a*c))/(a*2)
    x2 = (-b-sqrt(b**2 - 4*a*c))/(a*2)
    return x1, x2

a = 2
b = 7
c = -15

#print("les solutions de", a,"x² +",b,"x +",c," sont :", quad(a,b,c))
