n1 = input("Digite um valor: ")
print(type(n1))
#n1 vai ser do tipo str

n2 = int(input("Digite um valor: "))
print(type(n2))
#n2 vai ser do tipo int

## Para somar dois inteiros deve-se declarar o mesmo como int antes do input
## Caso contrario a soma de 5+3 seria exibida como 53 ao invés de 8


#Microexercicio 1

x = int(input("Digite um valor:"))
y = int(input("Digite outro valor"))

r = x + y

print("A soma entre{} ".format(x),"e{}".format(y)," eh: {}".format(r))

#Outros jeitos:
# print(" A soma entre", x, "e" , y, " vale ", r)
# print(" A soma entre {} e {} vale {}".format(x, y, r))