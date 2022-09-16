#Exercício Python 009: Faça um programa que leia
#um número Inteiro qualquer e mostre na tela a sua tabuada.


num = int(input('Digite um número inteiro para ver sua tabuada:'))
for cont in range (0,11):
    tab = cont * num
    print('{} X {} = {}' .format(num,cont,tab))
