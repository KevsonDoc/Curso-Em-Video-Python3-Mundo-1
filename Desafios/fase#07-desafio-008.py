# Escreva um programa que leia um valor em metros e o exiba convertidos
# em centimetros e milimetros
medida = float(input('Digite quantos metros deseja comverter: '))
cm = medida * 100
mm = medida * 1000
dm = medida * 10
dam = medida * 0.1
hm = medida * 0.01
km = medida * 0.001
print('A medida de {}m corresponde a \n{}mm \n{}cm \n{}dm \n{}m \n{}dam \n{}hm \n{}km'.format(medida, mm, cm, dm, medida, dam, hm, km))