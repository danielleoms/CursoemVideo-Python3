"""
import <NOME DO MÓDULO> | Importa tudo contido no módulo
from <NOME DO MÓDULO> import <NOME DA FUNÇÃO> | Importa uma função específica do módulo
from <NOME DO MÓDULO> import <NOME DA FUNÇÃO 1>, <NOME DA FUNÇÃO 2> | Importa duas ou mais funções específicas do módulo
Exemplos:
import math
from math import sqrt
from math import sqrt, ceil
Algumas Funções do Módulo math:
ceil - Arredonda o valor para cima
floor - Arredonda o valor para baixo
trunc
pow
sqrt
factorial

"""

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
