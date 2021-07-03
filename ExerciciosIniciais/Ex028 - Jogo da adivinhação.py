import time
from random import randint
from time import sleep
computador = randint(0, 5)

print("-="*40)
print("Vou pensar em um número entre 0 e 5. Tente adivinhar...")
print("-="*40)

num = int(input("Em que número eu pensei? "))
print("PROCESSANDO...")
time.sleep(1)

if num == computador:
    print("PARABENS! Voce ganhou!!")
else:
    print("GANHEI! Eu pensei no número {} e não no {} ".format(computador, num))
