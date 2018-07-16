numero = int(input("Digite um número inteiro: "))

Primo = True
count = 2

if (numero == 1):
    Primo = False
    
while Primo and (numero != count):
    if (numero % count == 0):
        Primo = False
    count += 1

if Primo:
    print ("primo")
else:
    print ("não primo")
    
    

