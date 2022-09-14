# Operadores aritméticos

# + adição
# - subtração
# * multiplicação
# / divisão
# ** potencia
# // divisão inteira
# % módulo: resto da divisão


n1 = int(input('Um valor:'))
n2 = int(input('Outro valor:'))
s = n1 + n2
m = n1 * 2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma vale {}, \n o produto é {} e a divisão é {:.3f}.' .format(s, m, d), end=' ')
print('Divisão inteira {} e potência {}' .format(di,e))

# \n quebra a linha e end=' ' junta linha dos prints

