#Exercício Python 52: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

núm = int(input('Digite um número: '))
tot = 0
for c in range(1, núm +1):
    if núm % c == 0:
        print('\033[33m', end=' ') #\033[33m destacar em cor amarela
        tot += 1
    else:
        print('\033[31m', end=' ') #\033[31m destacar em cor vermelha
    print('{}'.format(c), end=' ')
print('\n\033[mO número {} foi divível {} vezes.' .format(núm, tot)) #\033[m zerar a cor
if tot == 2:
    print('E por isso ele é PRIMO')
else:
    print('E por isso ele NÃO é primo')
