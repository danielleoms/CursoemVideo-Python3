#Exercício Python 11: Faça um programa que leia a largura e a altura de uma parede em metros,
# calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

lar = float(input('Largura da parede:'))
al = float(input('Altura da parede:'))
area = lar * al
tinta = area/2

print('Sua parede tem a dimensão de {} X {} e sua área é de {}m². \nPara pintar essa parede, você precisará de {}l de tinta.' .format(lar,al,area, tinta))
