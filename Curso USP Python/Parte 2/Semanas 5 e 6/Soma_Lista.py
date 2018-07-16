def soma_lista (lista):
    for i in range (len(lista)):
        assert type(lista[i])==int
    if len(lista) == 1:
        return lista[0]
    else:
        return lista[0] + soma_lista(lista[1:])
    
        
