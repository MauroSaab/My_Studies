def éPrimo(k):
    Primo = True    
    count = 2
       
    while Primo and (k != count):
        if (k % count == 0):
            Primo = False
        count += 1
    return Primo

def maior_primo(i):
    
    while (éPrimo(i)==False):
        i -= 1
    return i

x = 0

while (x<2):
    x = int(input("Digite um número inteiro maior ou igual a 2: "))
    
print (maior_primo(x))
