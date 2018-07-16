n = int(input("Digite o primeiro numero: "))
k = int(input("Digite o segundo numero: "))

def fatorial (x):
    fat = 1
    while (x>1):
        fat = fat*x
        x -= 1
    return fat

binomial = ((fatorial(n))/(fatorial(k)*(fatorial(n-k))))

print (binomial)
