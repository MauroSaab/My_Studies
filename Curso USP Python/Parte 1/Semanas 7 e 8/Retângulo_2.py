colunas_input = int(input("digite a largura: "))
linhas_input = int(input("digite a altura: "))

coluna = 1
linha = 1

while (linha <= linhas_input):
    while (coluna <= colunas_input):
        if (coluna == 1 or coluna == colunas_input):
            print ("#", end = "")
        elif (coluna != 1 and coluna != colunas_input and linha == 1):
            print ("#", end = "") 
        elif (coluna != 1 and coluna != colunas_input and linha == linhas_input):
            print ("#", end = "")
        else:
            print (" ", end = "")
            
        coluna += 1
    print ()
    coluna = 1
    linha += 1
        
