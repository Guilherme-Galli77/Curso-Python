from random import shuffle


a = str(input("Primeiro aluno: "))
b = str(input("Segundo aluno: "))
c = str(input("Terceiro aluno: "))
d = str(input("Quarto aluno: "))
lista = [a,b,c,d]
shuffle(lista)

print("O aluno escolhido foi {}".format(lista))
