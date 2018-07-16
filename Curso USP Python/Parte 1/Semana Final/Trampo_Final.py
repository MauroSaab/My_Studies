import re

def le_assinatura():
  '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
  print("Bem-vindo ao detector automático de COH-PIAH.")

  wal = float(input("Entre o Tamanho Medio de Palavra:"))
  ttr = float(input("Entre a Relação Type-Token:"))
  hlr = float(input("Entre a Razão Hapax Legomana:"))
  sal = float(input("Entre o Tamanho Médio de Sentença:"))
  sac = float(input("Entre a Complexidade Média da Sentença:"))
  pal = float(input("Entre o Tamanho Medio de Frase:"))

  as_a = [wal, trr, hlr, sal, sac, pal]
  
  return as_a

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
  '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
  sentencas = re.split(r'[.!?]+', texto)
  if sentencas[-1] == '':
      del sentencas[-1]
      return sentencas

def separa_frases(sentenca):
  '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
  return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
  '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
  return frase.split()

def n_palavras_unicas(lista_palavras):
  '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
  freq = dict()
  unicas = 0
  for palavra in lista_palavras:
    p = palavra.lower()
    if p in freq:           # SE A PALAVRA JÁ ESTIVER NO REGISTRO
      if freq[p] == 1:      # SE É A SEGUNDA VEZ QUE É ENCONTRADA  
          unicas -= 1           # ENTÃO ELA NÃO É MAIS UNICA
      freq[p] += 1          # SUA FREQUENCIA EH AUMENTADA
    else:
      freq[p] = 1           # SE A PALAVRA NAO ESTIVER NO REGISTRO
      unicas += 1           # ELA EH ACRESCENTADA COMO UNICA

  return unicas        

def n_palavras_diferentes(lista_palavras):
  '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
  freq = dict()
  for palavra in lista_palavras:
    p = palavra.lower()
    if p in freq:
        freq[p] += 1
    else:
        freq[p] = 1

  return len(freq)

def compara_assinatura(as_a, as_b):
  '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
  pass

def calcula_assinatura(texto):
  '''Essa funcao recebe um texto e deve devolver a assinatura do texto.'''

  sentencas = separa_sentencas(texto)       # PREENCHE O ARRAY SENTENCAS COM TODAS AS SENTENCAS DIGITADAS
  num_de_sentencas = len(sentencas)

  frases_1 = []
  frases_2 = []
    
  for sentenca in sentencas:                  # A PARTIR DAS SENTENÇAS:
      frases_1 = (separa_frases(sentenca))  
      for frase in frases_1:
          frases_2.append(frase)              # PREENCHE O ARRAY FRASES_2 COM TODAS AS FRASES DIGITADAS.

  num_de_frases = len(frases_2)

  palavras_1 = []
  palavras_2 = []

  for frase in frases_2:                      # A PARTIR DAS FRASES:
      palavras_1 = (separa_palavras(frase))
      for palavra in palavras_1:
          palavras_2.append(palavra)          # PREENCHE O ARRAY PALAVRAS_2 COM TODAS AS PALAVRAS DIGITADAS.

  num_de_palavras = len(palavras_2)

  




    



  pass

def avalia_textos(textos, ass_cp):
  '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
  pass
