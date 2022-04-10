# Desafio 020 - O mesmo professor do desafio enterior quer sortear a rodem de apresentação
# de trabalhos dos alunos. Faça um programa que leia o nome dos quatros alunos e mostre a
# ordem sorteada.
import random
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3, n4]

#Embaralha dentro da lista
random.shuffle(lista)
print('A orde de apresentação será: ')
print(lista)
