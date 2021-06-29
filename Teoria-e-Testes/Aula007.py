# Ver anotação pagina 1

#Equivalentes:
# 4**3 e pow(4,3)

print("oi"*5)
print('='*20)

n1 = int(input("Um valor: "))
n2 = int(input("Outro valor: "))

s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

print("A soma vale {}, \n o produto {}, a divisao {:.3f}".format(s, m, d), end=" --> ")
print("Divisão Inteira {} e potencia {}".format(di, e))

