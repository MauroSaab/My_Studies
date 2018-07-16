numero = int(input("Digite seu número: "))

soma = 0

while (numero > 0):
    last = numero % 10
    soma = soma + last
    numero = numero // 10
    
print (soma)
