#Exercício Python 010: Crie um programa que leia quanto
# dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

d = float(input('Cotação do dólar hoje:'))
dc = float(input('Quanto dinheiro você tem na carteira? R$'))
c = d * dc

print('Com R${} você pode comprar ${}.' .format(dc,c))
