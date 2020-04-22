#Desafio 006 - Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada
n1 = int(input('Digite um número: '))
r = n1 * 2
a = n1 * 3
# Os parenteses forçam a resolver primeiro o que estiver dentro deles
b = n1 ** (1/2)
print('O dobro de {} é {}.'.format(n1, r))
print('O triplo de {} é {}.'.format(n1, a))
print('A raiz quadrada de {} é {}.'.format(n1, b))
