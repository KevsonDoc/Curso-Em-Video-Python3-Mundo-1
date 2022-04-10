#Desafio 007 - Desenvolva um programa que leia as duas notas de um aluno,
#calcule e mostre a média

nota1 = float(input('Digite a sua primeira nota: '))
nota2 = float(input('Digite a sua segunda nota: '))
r = (nota1 + nota2) / 2
print('Sua média entre {} e {} é: {}'.format(nota1, nota2, r))