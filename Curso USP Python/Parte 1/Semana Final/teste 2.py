import re

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


texto = "Olá! Este é o texto, de Mauro. Vamos ver se funciona?"


sentencas = separa_sentencas(texto)       # PREENCHE O ARRAY SENTENCAS COM TODAS AS SENTENCAS DIGITADAS
num_de_sentencas = len(sentencas)

i=0
while (i<(len(sentencas))):
    print ("Sentença ", i+1, ":", sentencas[i])
    i += 1

frases_1 = []
frases_2 = []
  
for sentenca in sentencas:                  # A PARTIR DAS SENTENÇAS:
    frases_1 = (separa_frases(sentenca))  
    for frase in frases_1:
        frases_2.append(frase)              # PREENCHE O ARRAY FRASES_2 COM TODAS AS FRASES DIGITADAS.

i=0
while (i<len(frases_2)):
    print ("Frase ", i+1, ":", frases_2[i])
    i += 1

palavras_1 = []
palavras_2 = []

for frase in frases_2:                      # A PARTIR DAS FRASES:
    palavras_1 = (separa_palavras(frase))
    for palavra in palavras_1:
        palavras_2.append(palavra)          # PREENCHE O ARRAY PALAVRAS_2 COM TODAS AS PALAVRAS DIGITADAS.

i=0
while (i<len(palavras_2)):
    print ("Palavra", i+1, ":", palavras_2[i])
    i += 1


