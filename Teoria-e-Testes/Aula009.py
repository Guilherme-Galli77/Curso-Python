frase = "Curso em Video Python"
print(frase)
print(frase[3]) #indice 3 --> lembrando que começa em 0 na letra C
print(frase[3:13]) #De 3 até o indice 12
print(frase[:13]) #Do inicio até o indice 12
print(frase[13:]) #Do indice 13 ate o final
print(frase[1:15]) # Do indice 1 até o 15
print(frase[0:15]) # Do indice 0 até o 15
print(frase[0:15:2]) # Vai de 2 em dois, exemplo SNSNSNS
print(frase[0:15:3]) # Exemplo SNNSNNSNN
print(frase[::2]) # De 2 em 2 string inteira

print("""ESTE
EH
UM
PRINT
DE VARIAS
LINHAS""")


print(frase.count("o")) #Conta os "o" na frase, lembrando que "o" é diferente de "O"
print(frase.count("o", 0, 13)) #Conta os "o" na frase do index 0 ao 13
print(frase.upper()) #Joga tudo pra maisculo e .lower() joga pra minusculo
print(frase.upper().count("O")) #Joga pra maisculo e depois conta os "O"
print(frase.capitalize()) #Deixa apenas a primeira letra maiscula
print(frase.title()) #Todas as primeiras letras de cada palavra ficam maisculas

print(len(frase)) #tamanho da frase #Conta os " "

print(len(frase.strip())) #frase.strip remove os espaços antes e depois
print(frase.lstrip()) #lstrip remove espaços a esquerda
print(frase.rstrip()) #rstrip remove espaços a direita

print(frase.replace("o", "z")) #substitui um caracter ou frase por outro
print(frase[0]) #mostra a primeira letra

# Não posso mudar um conteudo de uma frase usando "x" = frase[0]
#O replace muda em uma instancia, para mudar definitivamente deve-se usar frase = frase.replace(......)

print("Curso" in frase) #Ver se "Curso" esta na frase
print(frase.find("Curso")) #Retorna o index da string procurada, se não existir ele retorna -1
print((frase.lower().find("video"))) #Busca em uma string transformada pra minusculo

print(frase.split()) #Separa as palavras em varias outras frases com index proprios
dividido = frase.split() #cada palavra vai ter um index na lista
print(dividido[0]) #Primeira palavra da lista(index 0)--> Curso
print(dividido[2][3]) #Pega a palavra divida index 2 que é video e exibe a letra no index 3 dessa palavra