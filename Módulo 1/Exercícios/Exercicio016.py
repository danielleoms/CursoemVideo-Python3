#Exercício Python 16: Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
#O método Math. trunc() retorna a parte inteira de um número, descartando suas casas decimais

# utilizando import math.:

import math
num = float(input('Digite um número:'))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, math.trunc(num)))
#O método Math. trunc() retorna a parte inteira de um número, descartando suas casas decimais

# utilizando from math import:

from math import trunc
num = float(input('Digite um número:'))
print('O valor digitado foi {} e a sua porção inteira é {}' .format(num, trunc(num)))

#utilizando função int

num = float(input('Digite um número:'))
print('O valor digitado foi {} e a sua porção inteira é {}' .format(num, int(num)))
