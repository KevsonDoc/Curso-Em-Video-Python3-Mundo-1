# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, cm 5 % de descont
pProduto = float(input('Digite o preço do produto?: R$ '))
r =pProduto - (pProduto * 5 / 100)
print('O valor do produto com 5% de desconto é: R${:.2f} R$'.format(r))
