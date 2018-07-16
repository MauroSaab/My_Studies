numero = int(input("Digite um número inteiro: "))

ultimo = numero % 10
flag = 0

while (numero > 0):
    if (numero//10 == 0):
        break
    penultimo = ((numero // 10) % 10)
    if (ultimo == penultimo):
        print ("sim")
        flag = 1
        break
    else:
        ultimo = penultimo
    numero = numero // 10
    ultimo = numero % 10

if (flag == 0):
    print ("não")
