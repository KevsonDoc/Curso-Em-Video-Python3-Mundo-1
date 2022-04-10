# Escreva um programa qu leia o salário de um funcionário e calcule o valor de seu amento.
# Para salários superior a R$ 1.250,00, calcule um aument de 10%. Para os inferiores ou,
# o aumento é de 15%.

salario = float(input('Digite o valor do seu salário: '))
if salario < 1250:
    salario = salario + (salario * 0.15)
else:
    salario = salario + (salario * 0.10)
print('O valor do seu novo salario é {}'.format(salario))
