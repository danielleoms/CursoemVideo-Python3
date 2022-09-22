#Exercício Python 17: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.  Calcule e mostre o comprimento da hipotenusa.
# Fórmula do comprimento da hipotenusa: a² + b² = c²


# Utilizando a fórmula matemática:

co = float(input('Comprimento do cateto oposto:'))
ca = float(input('Comprimento do cato adjacente:'))
hi  = (co ** 2 + ca ** 2) ** (1/2)

print('O comprimento da hipotenusa é {:.2f}' .format(hi) )

# Utilizando import math:

import math
co = float(input('\nComprimento do cateto oposto:'))
ca = float(input('Comprimento do cato adjacente:'))
hi = math.hypot(co, ca)

print('O comprimento da hipotenusa é {:.2f}' .format(hi) )

# Utilizando from math import:

from math import hypot
co = float(input('\nComprimento do cateto oposto:'))
ca = float(input('Comprimento do cato adjacente:'))
hi = hypot(co, ca)
print('O comprimento da hipotenusa é {:.2f}' .format(hi) )
