# Desafio 017 - Faça um programa que leia o comprimento do cateto oposto e do
# cateto adjacente de um triaângulo retângulo, e culcule e mostre o comprimento da hipotenusa
import math
cOposto = float(input('Digite o tamanho do cateto oposto: '))
cAdjacente = float(input('Digite o tamnho do cateto adjacente: '))
print('O tamho da Hipotenusa é {:.2f} .'.format(math.hypot(cOposto, cAdjacente)))