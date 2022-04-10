# Importando a biblioteca matemática (math)

import math

# Calculando raiz quadrada
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {:.2f}'.format(num, raiz))

# math.ceil() - Arredonda o valor para cima
print('A raiz de {} é igual a {}.'.format(num, math.ceil(raiz)))

# math.floor() - Arredonda o valor para baixo
print('A raiz de {} é igual a {}.'.format(num, math.floor(raiz)))

print('=' * 50)

# Importando apenas uma das funções existentes da bibloteca matematica

from math import sqrt, floor, ceil

num2 = int(input('Digite um número: '))
print('A raiz de {} é igul a {:.2f}\n A raiz de {} é igul a {}\n A raiz de {} é igul a {}.'.format(num, sqrt(num2), num, ceil(sqrt(num2)), num, floor(sqrt(num2))))
print('=' * 50)

# Inportando biblioteca Random
import random
num3 = random.random()
print(num3,'\n', '=' * 50)

# Gerando um número inteiro de 1 a 10
num4 = random.randint(1, 10)
print(num4)

import emoji
print(emoji.emojize("Hello World :earth_americas:", use_aliases=True))
