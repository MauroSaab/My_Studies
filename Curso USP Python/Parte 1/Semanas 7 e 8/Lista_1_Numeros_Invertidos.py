x=1
index = 0
list = []

while (x != 0):
    x = int(input("Digite um número inteiro ou digite zero para terminar: "))
    list.append(x)

del list[-1]        
printindex = len(list)

while (printindex > 0):
    print (list[printindex-1])
    printindex -= 1
        
    
