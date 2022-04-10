# Escreva um programa que leia a velcidade de um carro. Se ele ultrapassar 80 Km/h, mostre
# menssagem dizendo que ele foi multado. A multa vai custar R$ 7,00 por cada Km acima do
# limite.

velocidade = float(input('Digite a velocidade atual do carro em Km/h: '))

if velocidade > 80:
    print('MULTADO! \nVocê excedeu o limite permitido que é de 80 Km:')
    multa = 7 * (velocidade - 80.0)
    print('Valor da multa {} R$.'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')
