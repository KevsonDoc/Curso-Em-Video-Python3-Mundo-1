#Exercício 01
nome = input('Qual é oseu nome? ')
#Direita
print('Prazer em te conhecer {:<20}!'.format(nome))
#Esquerda
print('Prazer em te conhecer {:>20}!'.format(nome))
#Centralizado
print('Prazer em te conhecer {:^20}!'.format(nome))

print('Prazer em te conhecer {:=^20}!'.format(nome))

n1 = int(input('Digite um valor '))
n2 = int(input('Digite outro valor '))

a = n1+n2
b = n1*n2
c = n1 / n2
d = n1 // n2
e = n1 ** n2
print('A soma é: {}'.format(a))
print('A multiplicação é: {}'.format(b))
#com 3 casas decimais e flutuantes usando {:.3f}
print('A divisão é: {:.3f}'.format(c), '\n\n\n')
print('A divisão inteira é: {}'.format(d), end=' ')
print('O resultado da potênciação é: {}'.format(e))


#Para continuar na mesma linha colocar uma , e end' ' como na linha 24
#para quebrar uma linha utiliza-se o (\n)
