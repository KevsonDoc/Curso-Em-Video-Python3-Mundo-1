# Dsafio 10 - Crie um programa que leia quanto dinheiro uma pessoa tem na carteirar e mostre quantos
# dólarea ela pode comprar
carteira = float(input('Digite queantos reais você tem na carteira: R$'))
total = carteira / 3.27
print('-' * 50)
print('Com R${:.2f} você pode comprar US${:.2f}'.format(carteira, total))
