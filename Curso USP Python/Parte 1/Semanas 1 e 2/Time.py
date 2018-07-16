Seg = input ("Por favor, entre com o número de segundos que deseja converter: ")

SegundosInput = int(Seg)

Dias = SegundosInput // 86400
SegundosRestantes = SegundosInput % 86400

Horas = SegundosRestantes // 3600
SegundosRestantes = SegundosRestantes % 3600

Minutos = SegundosRestantes // 60
SegundosRestantes = SegundosRestantes % 60

print (Dias, "dias,", Horas, "horas,", Minutos, "minutos e", SegundosRestantes, "segundos.")

