l = float(input("Largura da parede: "))
a = float(input("Altura da parede: "))

area = l*a
print("Sua parede tem dimensão de {} X {} e sua area é de {} m2 ".format(l, a, area))

L = area/2
print("Para pintar essa parede, você precisará de {:.2f}L de tinta.".format(L))
