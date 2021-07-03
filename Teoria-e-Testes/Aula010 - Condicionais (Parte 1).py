#Exemplo 1
x = int(input("Digite 0 ou 1: "))
if x == 1: #So vai exibir se o numero digitado for 1
    print("Numero certo")


#Exemplo 2
nome = str(input("Qual é o seu nome? "))
if nome == "Guilherme":
    print("Que nome lindo você tem!")
else:
    print("Olá pessoa!")

print("Bom dia {} ".format(nome))

#Exemplo 3

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
m = (n1+n2)/2
print("A sua média foi {:.1f}".format(m))
if m >= 6.0:
    print("Aprovado!")
else:
    print("Reprovado!")

# Usando uma condição simplificada em 1 linha
print("Parabéns" if m >=6 else "Estude mais!")


