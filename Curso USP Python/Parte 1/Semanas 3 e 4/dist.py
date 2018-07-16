import math

num1 = int(input("Digite a coordenada x do primeiro ponto:"))
num2 = int(input("Digite a coordenada y do primeiro ponto:"))
num3 = int(input("Digite a coordenada x do segundo ponto:"))
num4 = int(input("Digite a coordenada y do segundo ponto:"))

dist = math.sqrt(((num1-num3)**2)+((num2-num4)**2))

if dist >= 10:
    print ("longe")
else:
    print ("perto")


