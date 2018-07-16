colunas_input = int(input("digite a largura: "))
linhas_input = int(input("digite a altura: "))

coluna = 1
linha = 1

while (linha <= linhas_input):
    while (coluna <= colunas_input):
        print ("#", end = "")
        coluna += 1
    print()
    coluna = 1
    linha += 1
        
