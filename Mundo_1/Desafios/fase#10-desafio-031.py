# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da
# passagem, cobrando R$ 0,50  por Km para viagen de até 200 Km e R$ 0,45 para viagens mais
# longas.

distancia = float(input('Qual a distância da viagem e Km: '))
if distancia <= 200:
    n = distancia * 0.50
    print('Para a distância {} o preço é {} R$.'.format(distancia, n))
else:
    f = distancia * 0.45
    print('Para a distância {} o preço é {} R$.'.format(distancia, f))

