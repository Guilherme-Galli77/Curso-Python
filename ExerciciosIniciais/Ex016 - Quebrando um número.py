from math import trunc
numero = float(input("Digite um número: "))
print("O valor digitado foi {} e sua porção inteira é {} ".format(numero,trunc(numero)))

# Metodo sem math

num = float(input("Digite um valor: "))
resultado = num//1
print("O valor digitado foi {} e sua porção inteira é {:.0f} ".format(num, resultado))
# No lugar de resultado pode usar int(num)
