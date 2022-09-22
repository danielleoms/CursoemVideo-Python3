# Exercício Python 20: O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

# Utilizando import random
import random
a1 = str(input('Primeiro aluno:'))
a2 = str(input('Segundo aluno:'))
a3 = str(input('Terceiro aluno:'))
a4 = str(input('Quarto aluno:'))
lista = [a1, a2, a3, a4] #quando for criar uma lista ela fica em colchetes.

random.shuffle(lista) #random.shuffle embaralha a lista
print('A ordem de apresentação será')
print(lista)

# Utilizando from random import choice

from random import shuffle
a1 = str(input('Primeiro aluno:'))
a2 = str(input('Segundo aluno:'))
a3 = str(input('Terceiro aluno:'))
a4 = str(input('Quarto aluno:'))
lista = [a1, a2, a3, a4] #quando for criar uma lista ela fica em colchetes.

shuffle(lista) #random.shuffle embaralha a lista
print('A ordem de apresentação será')
print(lista)
