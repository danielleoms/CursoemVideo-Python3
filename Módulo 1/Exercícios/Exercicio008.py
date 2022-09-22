## Exercício Python 008: Escreva um programa que leia um valor em metros e
# o exiba convertido em centímetros e milímetros.

d = float(input('Digite uma distância em metro:'))
km = d / 1000 # quilômetro
hm = d / 100 # hectômetro
dam = d / 10 # decâmetro
m = d # metro
dm = d * 10 # decímetro
cm = d * 100 # centímetro
mm = d * 1000 # milímetro
print('A distância de {}m corresponde a: \n{:.3f}km \n{:.2f}hm \n{:.1f}dam \n{:.0f}dm \n{:.0f}cm \n{:.0f}mm'.format(m, km, hm, dam, dm, cm, mm))
