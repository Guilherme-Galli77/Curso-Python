# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.
cidade = str(input("Em que cidade você nasceu? ")).strip().capitalize()
print("Santo" in cidade)
# Pode fazer desse jeito:
# print(cidade[:5].captalize() == "Santo")
