def vogal (k):
    Vogal = False
    if (k == "a" or k == "A" or k == "e" or k == "E" or k == "i" or k == "I"):
        Vogal = True
    if (k == "o" or k == "O" or k == "u" or k == "U"):
        Vogal = True
    return Vogal

string = input ("Digite um caractere: ")

print (vogal(string))
    
