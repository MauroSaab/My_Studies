x = 1
while (x>0):
    x = int(input("Digite um número para calcular seu fatorial: "))
    if (x<0):
        print ("Número inválido. Programa encerrado.")
        break
    count = 1
    fat = 1
    while (count <= x):
        fat = fat * count
        count += 1
    print (fat)
    count = 1
        
