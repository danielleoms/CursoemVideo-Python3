"""Exercício Python 42: Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

– EQUILÁTERO: todos os lados iguais

– ISÓSCELES: dois lados iguais, um diferente

– ESCALENO: todos os lados diferentes """

a = float(input('Primeiro segmento:'))
b = float(input('Segundo segmento:'))
c = float(input('Terceiro segmento:'))

if a > b + c or b > c + a or c > a + b:
    print('Os segmentos não podem formar um triângulo.')

elif a == b == c:
    print('Os segmentos podem formar um triângulo.\nO triângulo formado será equilátero.')

elif a != b != c != a:
    print('Os segmentos podem formar um triângulo.\nO triângulo formado será escaleno.')

elif a == b != c or b == c != a or a == c != b:
    print('Os segmentos podem formar um triângulo.\nO triângulo formado será isósceles.')

print('-=-' *30)
# RESOLUÇÃO DO GUANABARA

r1 = float(input('Primeiro segmento:'))
r2 = float(input('Segundo segmento:'))
r3 = float(input('Terceiro segmento:'))

if r1 < r2 + r3 or r2 < r1 + r3 or r3 < r1 + r2:
    print('Os segmentos podem formar um triângulo.')
    if r1 == r2 == r3:
        print('Ele será equilátero')
    elif r1 != r2 != r3 != r1:
        print('Ele será escaleno')
    else:
        print('Ele será isósceles')
else:
    print('Os segmentos não podem formar um triângulo.')
