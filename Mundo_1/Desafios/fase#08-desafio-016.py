# Desafio 016 - Crie programa que leia um número real qualquer e mostre na tela a sua
# porção inteira
from math import trunc
num = float(input('Digite um valor: '))
#Utilizando o método o trunc() da biblioteca math
print('O número {} tem a porção inteira {}'.format(num, trunc(num)))

#Utilizando uma função interna
print('O número {} tem a porção inteira {}'.format(num, int(num)))