def maximo (x,y):
    if (x>y):
        maxi = x
    else:
        maxi = y
    return (maxi)

x = int(input("Digite o primeiro número: "))
y = int(input("Digite o segundo número: "))

print (maximo(x,y))
