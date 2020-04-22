# Escreva um programa que faça computador "pensar" em um número inteiro entre 0 e 5 e peça
# O usuario tentar descobrir qual foi o número escolhido pelo computador. O programa deverá
# escrever na tela se o usuário venceu ou perdeu.

import random
print('Espere vou gerar um número de 0 a 5! \nPronto!')
numero = random.randint(0, 5)
entrada = int(input('Tende descobrir o número: '))

if numero == entrada:
    print('Parabéns! Você acertou.')
else:
    print('Ou não! \nVocê errou.')
print('O número gerado é {}'.format(numero))
