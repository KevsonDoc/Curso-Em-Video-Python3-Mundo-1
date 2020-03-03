# Desenvolva um programa que leia o comprimento de três retas e dig ao usuário se elas podem
# ou não formar um triângulo.

r1 = float(input('Primeiro segmanto: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

if r1 <r2 +r3 and r2 < r1 + r3 and r3 < r1 +r2:
    print('O segmento acima POMDE FORMAR UM triângulo!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo!')
