#Exercício Python 010: Crie um programa que leia quanto
# dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.


cotdol= float(input('Valor da cotação do dólar hoje em relação ao real:'))
di = float(input('Quantos reias (R$) você tem na carteira?'))
real = di / cotdol

print('Com R${}, você tem ${:.1f}.'.format(di,real))

