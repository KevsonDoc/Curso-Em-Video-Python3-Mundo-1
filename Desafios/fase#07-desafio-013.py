# Faça um algoritmo que leia p salário de um funcionário, com 15% de aumento
salario = int(input('Digite o valor do seu salário: R$ '))
r = salario + (salario * 15 / 100)
print('Seu novo salário com 15% de aumento é {:.2f} R$'.format(r))
