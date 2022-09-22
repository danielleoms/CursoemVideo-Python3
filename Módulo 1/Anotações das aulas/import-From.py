# import é uma função generalista

import math
num = int(input('Digite um número:'))
raiz = math.sqrt(num)
print('A raiz de um {} é igual a {:.2f}.' .format(num, raiz))

# from é um importação específica

from math import sqrt
num = int(input('Digite um número:'))
raiz = sqrt(num)
print('A raiz de um {} é igual a {:.2f}.' .format(num, raiz))
