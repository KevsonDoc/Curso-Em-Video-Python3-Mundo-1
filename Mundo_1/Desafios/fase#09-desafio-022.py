# Crie um programa que leia o nome completo de uma pessoa e mostre:
# - O nome com todas as letras maiúsculas - O nome com todas minúsculas - Quantos letras ao
# todo (Sem considerar os espaços). - Quantas letras tem o primeiro nome.
nome = str(input('Digite o seu nome completo: ')).strip()
print('Seu nome em maúsculas {}'.format(nome.upper()))
print('Seu nome em minúsculas {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
