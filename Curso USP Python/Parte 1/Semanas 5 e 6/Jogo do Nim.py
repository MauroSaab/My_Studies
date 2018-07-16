def computador_escolhe_jogada (n, m):

    aux = 0
    flag = 0
    while (aux <= n and n >= m):
        if ((n-aux)%(m+1) == 0):
            flag = 1
            break
        aux += 1

    if (flag):
        jogada = aux
    elif (m>n):
        jogada = n
    else:
        jogada = m

    if (jogada == 1):
        print ("O computador tirou 1 peça. Restam", n-1, "peças.")
    else:
        print ("O computador tirou", jogada, "peças. Restam", n-jogada, "peças.", '\n')
        
    return jogada
           
def usuario_escolhe_jogada (n, m):

    jogada = int(input("Quantas peças você vai tirar? "))
    while ((jogada > m) or (jogada <= 0) or (jogada > n)):
        print ("Oops! Jogada Inválida! Tente de novo.", '\n')
        jogada = int(input("Quantas peças você vai tirar? "))   

    if (jogada == 1):
        print ("Você tirou 1 peça. Restam", n-1, " peças.", '\n')
    else:
        print ("Você tirou", jogada, "peças. Restam", n-jogada, "peças.", '\n')
    
    return jogada
           
def partida ():

    print ("Quantas peças no tabuleiro?")    # 9
    n = int(input())
    print ("Limite de peças por jogada?")   # 2
    m = int(input())

    AI_Turn = False
    Player_Turn = False
    
    if (n % (m+1) == 0):
        Player_Turn = True
        print ("Você começa", '\n')
    else:
        AI_Turn = True
        print ("O computador começa", '\n')

    while (n>0):  
        if (AI_Turn):
            n -= computador_escolhe_jogada(n,m)
            AI_Turn = False
            Player_Turn = True
        else:
            n -= usuario_escolhe_jogada(n,m)
            Player_Turn = False
            AI_Turn = True

    if (n == 0):
        if (not AI_Turn):
            print ("Fim de Jogo! O computador venceu!", '\n')
            return 1
        else:
            print ("Parabéns! Você venceu!", '\n')
            return 2
    
def campeonato():

    AI_Wins = 0
    Player_Wins = 0
    count = 1
    while (count < 4):
        print ('\n', "**** Rodada ", count, "****")
        if (partida()==1):
            AI_Wins += 1
            count += 1
        else:
            Player_Wins +=1
            count += 1
    
    print ("**** Final do campeonato! ****")
    print ("Placar: Você ", Player_Wins, " X ", AI_Wins, " Computador")

def main():
    print ("Bem-vindo ao jogo do NIM! Escolha:", '\n')
    print ("1 - para jogar uma partida isolada")
    print ("2 - para jogar um campeonato")
    entry = int(input())
    while (entry < 1 or entry > 2):
        print ("Opção inválida. Por favor escolha 1 ou 2")
        entry = int(input())
    if (entry == 1):
        partida()
    else:
        campeonato()

main()
        
    

