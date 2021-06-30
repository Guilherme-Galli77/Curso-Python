#Importar tudo de math
#import math
#Importar apenas sqrt de math
#from math import sqrt
#Importar mais de uma coisa da math
#from math import sqrt, floor
import math
num = int(input("Digite um número: "))
raiz = math.sqrt(num)
print("A raiz de {} é igual a {} ".format(num, math.ceil(raiz)))
#math.ceil arredonda pra cima da virgula e floor pra baixo



import random
num = random.randint(1, 10)
print("Numero aleatorio {}".format(num))

import emoji
print(emoji.emojize('Ola Mundo :thumbsup:', use_aliases=True))
