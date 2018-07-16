coord_x = float(input("Digite a coordenada x"))
coord_y = float(input("Digite a coordenada y"))

if (coord_x < 0):
    coord_x_pos = -1 * coord_x
else:
    coord_x_pos = coord_x

Iris = False
Boca = False
Olho = False

if (coord_y >= 1 and coord_y <= 2 and coord_x_pos <= 3):
    Boca = True
    
if (coord_y > 5 and coord_y < 6 and coord_x_pos > 2 and coord_x_pos < 3):
    Iris = True

if (coord_y >= 4 and coord_y <= 7 and coord_x_pos >= 1 and coord_x_pos <= 4 and Iris == False):
    Olho = True
    
if (Olho == True or Boca == True):
    print ("fora")
else:
    print ("dentro")
