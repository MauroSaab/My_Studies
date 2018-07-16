def ordena(lista):

    fim = len(lista)
    for i in range (fim):
        for j in range (i+1, fim):
            if lista[j] < lista[i]:
                lista[i], lista[j] = lista[j], lista[i]
    return lista
        
