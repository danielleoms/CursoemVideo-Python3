## EXERCÍCIO 016: Quebrando um Número
## Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.

#Utilizando from math import 

import math
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}.'.format(num, math.trunc(num)))

#Utilizando from math import trunc

from math import trunc
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}.'.format(num, trunc(num)))

#Utilizando função inteiros 

num = float(input('Digite um valor: '))
print('O valor digitado foi {} e sua porção inteira é {}.'.format(num, int(num)))
