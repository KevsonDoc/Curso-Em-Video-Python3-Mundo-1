frase = 'Curso em Vídeo Python'
# mostra a 4 letra
print(frase[3])

# Exibe da 4 letra até a 12
print(frase[3:13])

# Não especificando o inicio e exibindo até a 12
print(frase[:13])

# Não especificando o final
print(frase[13:])

# Exibindo até n especificado pulando de n em n
print(frase[0:15:2])

print('=' * 50)

print("""Lorem
ipsum
vivamus
primis
quisque
lacus
quisque
orci
ultrices, placerat
inceptos
mauris sodales sagittis nisi nulla, donec viverra id tristique suspendisse netus, etiam orci per vestibulum aliquam.""")

# Conta quantos 'o' tem na minha frase
print(frase.count('o'))

# Colocar uma letra em maiusculo e conta quantos O maiusculos
print(frase.upper().count('O'))

# conta quatos caracteres tem
print(len(frase))

# remove espaços idesejáveis
frase = '            Curso em Vídeo Python          '
print(len(frase.strip()))

# Trocando frases por android
frase = frase.strip().replace('Python', 'Android')
print(frase)

print('Curso' in frase)

print(frase.find('Curso'))

# quebrando
print(frase.split())
divi = frase.split()
print(divi[0] [0])