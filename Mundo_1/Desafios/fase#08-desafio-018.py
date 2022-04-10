# Desafio 018 - Faça um programa que leia um ângulo qualquer e mostre na tela o valor
# de seno, e cosseno e tangente desse ângulo.
import math
angulo = float(input('Digite o tamanho do seu ângulo: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print('Para o ângulo {:.2f} temos seno {:.2f}, coseno {:.2f} e tangente {:.2f}'.format(angulo, seno, cosseno, tangente))

