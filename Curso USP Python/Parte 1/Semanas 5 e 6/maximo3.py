def maximo (x, y, z):
    if (x>=y and x>=z):
        return x
    elif (y>=x and y>=z):
        return y
    elif (z>=x and z>=y):
        return z

x = int(input("Digite o primeiro número: "))
y = int(input("Digite o segundo número: "))
z = int(input("Digite o terceiro número: "))

print (maximo(x,y,z))


