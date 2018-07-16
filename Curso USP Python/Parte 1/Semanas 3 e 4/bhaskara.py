a = float(input("Digite o primeiro coeficiente da Equação de Segundo Grau:"))
b = float(input("Digite o segundo coeficiente da Equação de Segundo Grau:"))
c = float(input("Digite o terceiro coeficiente da Equação de Segundo Grau:"))

import math

delta = b**2 - 4*a*c

if (delta > 0):
    r1 = (-b + math.sqrt(delta))/(2*a)
    r2 = (-b - math.sqrt(delta))/(2*a)
    if (r1 > r2):
        flag = r1
        r1 = r2
        r2 = flag
    print ("as raízes da equação são", r1, "e", r2)
elif (delta == 0):
    r1 = (-b/(2*a))
    print ("a raiz desta equação é", r1)
elif (delta < 0):
    print ("esta equação não possui raízes reais")
    
    
