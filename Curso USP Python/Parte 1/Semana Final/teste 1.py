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


texto = "NOSSA alegria diante dum sistema metafisico, nossa satisfação em presença duma construção do pensamento, em que a organização espiritual do mundo se mostra num conjunto lógico, coerente a harmônico, sempre dependem eminentemente da estética; têm a mesma origem que o prazer, que a alta satisfação, sempre serena afinal, que a atividade artística nos proporciona quando cria a ordem e a forma a nos permite abranger com a vista o caos da vida, dando-lhe transparência."

sentencas = separa_sentencas(texto)       # PREENCHE O ARRAY SENTENCAS COM TODAS AS SENTENCAS DIGITADAS
num_sentencas = len(sentencas)

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

num_frases = 0
num_caracteres = 0

while (num_frases<len(frases_2)):
  print ("Método Frases -> Caracteres: ", num_caracteres)
  num_caracteres += len(frases_2[num_frases])
  num_frases += 1
  
num_sentencas = 0
num_caracteres = 0

while (num_sentencas<=len(sentencas)):
  print ("Método Sentenças -> Caracteres: ", num_caracteres)
  num_caracteres += len(sentencas[num_sentencas])
  num_sentencas += 1

print ("Frases: ", num_frases)
print ("Tamanho Médio de Frase: ", num_caracteres/num_frases)
