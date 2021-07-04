# Exercício Python 35: Desenvolva um programa que leia o comprimento de três retas
# e diga ao usuário se elas podem ou não formar um triângulo.

a = float(input("Digite o tamanho do primeiro segmento: "))
b = float(input("Digite o tamanho do segundo segmento: "))
c = float(input("Digite o tamanho do terceiro segmento: "))

if a < b + c and b < a + c and c < a + b:
    print("Pode formar um triangulo! ")
else:
    print("Não forma triangulo! ")