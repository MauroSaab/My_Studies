import math

def éPrimo (x):
    count = 2
    Primo = True
    if (x==1):
        return False
    while (count <= math.sqrt(x) and Primo):
        if (x % count == 0):
            Primo = False
            return False
        count += 1
    return True

x = int(input())        
if (éPrimo(x) == False):
    print ("Não é Primo")
else:
    print ("É Primo")
    
