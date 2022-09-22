## Exercício Python 007: Desenvolva um programa que leia
# as duas notas de um aluno, calcule e mostre a sua média.

n1 = float(input('Primeira nota:'))
n2 = float(input('Segunda nota:'))
m = (n1 + n2) / 2

print('A sua média é {:.2f}' .format(m))
