import random

def lista_grande(n):
    lista = []
    i = 0
    while i < n:
        m = random.randint(-1000, 1000)
        lista.append(m)
        i += 1

    return lista
