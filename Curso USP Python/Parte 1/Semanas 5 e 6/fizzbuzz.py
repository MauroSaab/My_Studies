def fizzbuzz (k):
    if (k % 3 == 0 and k % 5 == 0):
        return ("FizzBuzz")
    elif (k % 3 == 0 and k % 5 != 0):
        return ("Fizz")
    elif (k % 5 == 0 and k % 3 != 0):
        return ("Buzz")
    elif (k % 3 != 0 and k % 5 != 0):
        return (k)

k = int(input("Digite um número inteiro: "))
print (fizzbuzz (k))
    
