print("\033[31mOla Mundo") #Letra vermelha
print("\033[31;43mOla Mundo") #Letra vermelha e fundo amarelo
print("\033[1;31;43mOla Mundo") #Letra vermelha e fundo amarelo (letras em negrito)
print("\033[4;30mOla Mundo\033[m") #Sublinhado

a = 3
b = 5
print("Os valores são \033[32m{}\033[m e \033[31m{}\033[m !!!!".format(a, b)) #a e b de cores diferentes
print("Os valores são \033[32;44m{}\033[m e \033[31;44m{}\033[m !!!!".format(a, b)) #fundo azul nas letras a e b

#2 maneira de printar

nome = "Guilherme"
print("Método diferente de printar, {}{}{} !!!!".format("\033[4;34m", nome, "\033[m"))

#3 maneira de printar

cores = {"limpa": "\033[m",
         "azul": "\033[34m",
         "amarelo":"\033[33m",
         "preto e branco": "\033[m"}

print("Método diferente de printar, {}{}{} !!!!".format(cores["amarelo"], nome, cores["limpa"]))


