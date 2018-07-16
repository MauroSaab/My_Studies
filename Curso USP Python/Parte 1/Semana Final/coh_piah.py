import re

def le_assinatura():
  '''A função lê os valores dos traços linguísticos do texto-modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''

  print("Bem-vindo ao detector automático de COH-PIAH.")

  wal = float(input("Entre o Tamanho Medio de Palavra:"))
  ttr = float(input("Entre a Relação Type-Token:"))
  hlr = float(input("Entre a Razão Hapax Legomana:"))
  sal = float(input("Entre o Tamanho Médio de Sentença:"))
  sac = float(input("Entre a Complexidade Média da Sentença:"))
  pal = float(input("Entre o Tamanho Médio de Frase:"))

  return [wal, ttr, hlr, sal, sac, pal]
  
def le_textos():
  i = 1
  textos = []
  texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
  while texto:
    textos.append(texto)
    i += 1
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

  return textos

def separa_sentencas(texto): 
  '''A função recebe um texto e devolve suas sentenças constituintes.'''
  sentencas = re.split(r'[.!?]+', texto)
  if sentencas[-1] == '':
      del sentencas[-1]
      return sentencas

def separa_frases(sentenca):
  '''A função recebe uma sentenca e devolve suas frases constituintes.'''
  return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
  '''A função recebe uma frase e devolve suas palavras constituintes.'''
  return frase.split()

def n_palavras_unicas(lista_palavras):
  '''A função recebe uma lista de palavras e devolve o número de palavras utilizadas uma unica vez.'''
  freq = dict()
  unicas = 0
  for palavra in lista_palavras:
    p = palavra.lower()
    if p in freq:           # SE A PALAVRA JÁ ESTIVER NO REGISTRO
      if freq[p] == 1:        # SE É A SEGUNDA VEZ QUE É ENCONTRADA 
          unicas -= 1           # ENTÃO ELA NÃO É MAIS ÚNICA.
      freq[p] += 1            # SUA FREQUENCIA EH AUMENTADA
    else:
      freq[p] = 1           # SE A PALAVRA NAO ESTIVER NO REGISTRO
      unicas += 1             # ELA É ACRESCENTADA COMO UNICA

  return unicas        

def n_palavras_diferentes(lista_palavras):
  '''A função recebe uma lista de palavras e devolve o número de palavras diferentes utilizadas.'''
  freq = dict()
  for palavra in lista_palavras:
    p = palavra.lower()
    if p in freq:
        freq[p] += 1
    else:
        freq[p] = 1

  return len(freq)

def calcula_assinatura(texto):
  '''A função recebe um texto e devolve uma lista contendo os seis parâmetros (a assinatura) do texto.'''

  sentencas = separa_sentencas(texto)       # PREENCHE O ARRAY SENTENCAS COM TODAS AS SENTENCAS DIGITADAS
  num_de_sentencas = len(sentencas)

  frases_1 = []
  frases_2 = []
    
  for sentenca in sentencas:                  # A PARTIR DAS SENTENÇAS:
      frases_1 = (separa_frases(sentenca))  
      for frase in frases_1:
          frases_2.append(frase)              # PREENCHE O ARRAY FRASES_2 COM TODAS AS FRASES DIGITADAS.

  palavras_1 = []
  palavras_2 = []

  for frase in frases_2:                      # A PARTIR DAS FRASES:
      palavras_1 = (separa_palavras(frase))
      for palavra in palavras_1:
          palavras_2.append(palavra)          # PREENCHE O ARRAY PALAVRAS_2 COM TODAS AS PALAVRAS DIGITADAS.

  num_de_palavras = len(palavras_2)

  ### WAL - TAMANHO MÉDIO DE PALAVRA

  num_palavras = 0 
  total_caracteres = 0
  while (num_palavras < len(palavras_2)):
    total_caracteres += len(palavras_2[num_palavras])
    num_palavras += 1

  WAL = total_caracteres/num_palavras

  ### TTR - RELAÇÃO TYPE-TOKEN

  palavras_diferentes = n_palavras_diferentes(palavras_2)

  TTR = palavras_diferentes/num_palavras

  ### HLR - RAZÃO HAPAX LEGOMANA

  palavras_unicas = n_palavras_unicas(palavras_2)

  HLR = palavras_unicas/num_palavras

  ### SAL - TAMANHO MÉDIO DE SENTENÇA

  num_sentencas = 0
  num_caracteres_sent = 0

  for sentenca in sentencas:
    num_caracteres_sent += len(sentenca)
  
  num_sentencas = len(sentencas)

  SAL = num_caracteres_sent/num_sentencas

  ### SAC - COMPLEXIDADE DE SENTENÇA

  num_frases = len(frases_2)
  
  SAC = num_frases/num_sentencas

  ### PAL - TAMANHO MÉDIO DE FRASE

  num_caracteres_frase = 0

  for frase in frases_2:
    num_caracteres_frase += len(frase)
  
  PAL = num_caracteres_frase/num_frases

  as_texto = [WAL, TTR, HLR, SAL, SAC, PAL]
  return (as_texto)

def compara_assinatura(as_a, as_b):
  '''A função recebe duas assinaturas de texto e devolve o grau de similaridade entre elas.'''

  diferenca = 0
  somatorio = 0

  for i in range(0,6):
    diferenca = as_a[i] - as_b[i]
    if diferenca < 0:
      diferenca = - diferenca
    somatorio += diferenca

  grau_de_similaridade = somatorio/6

  return grau_de_similaridade

def avalia_textos(textos_input, as_input):
  '''A função recebe uma lista de textos e a assinatura linguística e devolve o número (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''

  scores = []
  for texto in textos_input:
    as_texto = calcula_assinatura(texto)
    grau = compara_assinatura(as_input, as_texto)
    print ("Grau de similaridade do Texto: ", grau)
    scores.append(grau)
    print (scores)

  i = 0
  lowest_pos = 0
  lowest = scores[0]
  while i < len(scores):
    if scores[i] < lowest:
      lowest_pos = i
    i += 1

  return (lowest_pos+1)


as_input = le_assinatura()
textos_input = le_textos()


print ("O autor do texto", avalia_textos(textos_input, as_input), "está infectado com COH-PIAH")
    
  
  















  
