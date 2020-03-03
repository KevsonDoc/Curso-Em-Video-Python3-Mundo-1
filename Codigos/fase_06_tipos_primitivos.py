#Exercício 1
num1 = int(input('Digite um número: '))
num2 = int(input('Digite mais um número: '))
res = num1 + num2
print('Forma de concatenar no print:')
print('A soma entre', num1, ' e ', num2, ' é igual a: ', res)
print('Outra forma de concatenar:')

print('A soma vale {} e {} vale {}'.format(num1, num2, res))

#Exercício 2
n = input('Digite um valor: ')
print(n)
print(n.isnumeric())