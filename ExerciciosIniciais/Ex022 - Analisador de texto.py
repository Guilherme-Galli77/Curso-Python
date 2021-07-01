###Exercício Python 22: Crie um programa que leia o nome completo de uma pessoa e mostre:

#– O nome com todas as letras maiúsculas e minúsculas.

#– Quantas letras ao t0do (sem considerar espaços).

#– Quantas letras tem o primeiro nome.

nome = str(input("Digite seu nome completo: ")).strip()
print("Seu nome em maisculas é {} ".format(nome.upper()))
print("Seu nome em minusculas é {}".format(nome.lower()))
x = nome.replace(" ", "")
print("Seu nome tem ao todo {} letras".format(len(x)))
#print("Seu nome tem ao t0do {} letras".format(len(nome) - nome.count(" ")))
dividido = nome.split()
print("Seu primeiro nome é {} e ele tem {} letras".format(dividido[0], len(dividido[0])))
#print("Seu primeiro nome é {} e ele tem {} letras".format(nome.find(" ")))
