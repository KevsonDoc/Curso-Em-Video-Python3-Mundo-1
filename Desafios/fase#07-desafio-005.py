#Desafio 005 - Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e antecessor.
n1 = int(input('Digite um número: '))
a = n1 + 1
b = n1 - 1

print('O número sucessor de {} é {} e seu número antecessor é {}'.format(n1, a, b))
#ou
print('O número sucessor de {} é {} e seu número antecessor é {}'.format(n1, (n1 +1), (n1 - 1)))