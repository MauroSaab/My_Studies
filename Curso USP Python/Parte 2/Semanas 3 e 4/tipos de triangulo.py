class Triangulo:
    def __init__ (self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimetro(self):
        return (self.a+self.b+self.c)

    def tipo_lado(self):
        if self.a == self.b:
            if self.b == self.c:
                return "equilátero"
            else:
                return "isósceles"
        elif self.a == self.c:
            if self.b == self.c:
                return "equilátero"
            else:
                return "isósceles"
        else:
            return "escaleno"

    def retangulo(self):
        if self.a**2 + self.b**2 == self.c**2:
            return True
        elif self.b**2 + self.c**2 == self.c**2:
            return True
        elif self.a**2 + self.c**2 == self.b**2:
            return True
        else:
            return False
    
    def semelhantes(self,triangulo):
        lista1 = sorted([self.a, self.b, self.c])
        lista2 = sorted([triangulo.a, triangulo.b, triangulo.c])
        flag = 1

        if lista1[0] >= lista2[0]:
            for i in range (3):
                if lista1[i] % lista2[i] != 0:       
                    flag = 0
                    break
                
        if lista2[0] > lista1[0]:                 
            for i in range (3):
                if lista2[i] % lista1[i] != 0:
                    flag = 0
                    break

        if flag == 1:
            return True
        if flag == 0:
            return False

        
    
            
        
        
