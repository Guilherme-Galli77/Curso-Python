#Mostra o tipo primitivo e informaçoes sobre a entrada

x = input("Digite algo: ")

print("O tipo primitivo desse valor é ", type(x))
print("Só tem espaços? ", x.isspace())
print("È um número? ", x.isnumeric())
print("È alfabético? ", x.isalpha())
print("È alfanumérico? ", x.isalnum())
print("Está em maiusculas? ", x.isupper())
print("Está em minusculas?", x.islower())
print("Está capitalizada? ", x.istitle())

