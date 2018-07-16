def encontra_impares(lista):

    impares = []

    for i in range (len(lista)):
        assert type(lista[i])==int
               
    if len(lista) > 0:
        numero = lista.pop(0)
        if numero % 2 != 0:
            impares.append(numero)
        impares = impares + encontra_impares(lista)

    return impares
    
            
    
        
    
        
