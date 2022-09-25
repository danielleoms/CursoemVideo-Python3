
#Exercício Python 37: Escreva um programa em Python que leia um número inteiro qualquer e 
#peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

"""print('-=-' * 10)
num = int(input('Informe um número inteiro:'))
print('-=-' * 10)
print('Escolha uma das bases para conversão:')
print(' [ 1 ] para binário \n [ 2 ] para octal \n [ 3 ] para hexadecimal')
base = int(input('Sua opção:'))

if base == 1:
    print('O número {} em binário é {}.' .format(num, bin(num)))

elif base == 2:
    print('O número {} em octal é {}.'.format(num, oct(num)))

elif base == 3:
    print('O número {} em binário é {}' .format(num,hex(num)))

else:
    print('Não existe essa opção')"""

#Resolução do Guanabara

num = int(input('Digite um número inteiro:'))
print('''Escolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''') #utilizar três aspas para fazer um print em mais de uma linha
opção = int(input('Sua opção:'))
if opção == 1:
    print('{} convertido para binário é igual a {}.' .format(num, bin(num)[2:])) #usar o recuso de fatiamento para não aparecer o começo da resposta
elif opção == 2:
    print('{} convertido para octal é igual a {}.'.format(num, oct(num)[2:])) #usar o recuso de fatiamento para não aparecer o começo da resposta
elif opção == 3:
    print('{} convertido para hexadecimal é igual a {}.' .format(num, hex(num)[2:])) #usar o recuso de fatiamento para não aparecer o começo da resposta
else:
    print('Não existe essa opção.')
