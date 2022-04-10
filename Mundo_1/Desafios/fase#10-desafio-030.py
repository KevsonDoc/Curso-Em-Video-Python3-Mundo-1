# Crie um programa que leia um número iteiro e mostre na tela se ele é par uo impar.
numero = int(input('Digite um número que vou dizer se é impar ou pár: '))
if numero % 2 == 0:
    print('O número {} é par.'.format(numero))
else:
    print('O número {} é impar.'.format(numero))
