a = float(input("Digite o primeiro coeficiente da Equação de Segundo Grau:"))
b = float(input("Digite o segundo coeficiente da Equação de Segundo Grau:"))
c = float(input("Digite o terceiro coeficiente da Equação de Segundo Grau:"))

import math

def delta (a, b, c):
    delta = b**2 - 4*a*c
    return delta

def duas_raizes (delta):
    r1 = (-b + math.sqrt(delta(a,b,c)))/(2*a)
    r2 = (-b - math.sqrt(delta(a,b,c)))/(2*a)
    if (r1 > r2):
        flag = r1
        r1 = r2
        r2 = flag
    print ("as raízes da equação são", r1, "e", r2)

def uma_raiz (delta):
    r1 = (-b/(2*a))
    print ("a raiz desta equação é", r1)

def sem_raizes_reais():
    print ("esta equação não possui raízes reais")

if delta (a,b,c) > 0:
    duas_raizes (delta)
elif delta (a,b,c) == 0:
    uma_raiz (delta)
elif delta (a,b,c) < 0:
    sem_raizes_reais()
    
