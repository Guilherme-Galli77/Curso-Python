from math import sqrt

oposto = float(input("Comprimento do cateto oposto: "))
adjacente = float(input("Comprimento do cateto adjacente: "))
hip = sqrt((oposto**2)+(adjacente**2)) # Ao inves de usar sqrt posso usar **(1/2)

print("A hipotenusa vai medir {:.2f} ".format(hip))


#Metodo mais direto usando hypot
from math import hypot
hip2 = hypot(oposto, adjacente)
print("A hipotenusa vai medir {:.2f} ".format(hip2))
