numero = int(input("Digite um número inteiro: "))

soma = 0
last = 0

while (numero != 0):
    last = numero % 10
    soma = soma + last
    numero = numero//10

print (soma)
