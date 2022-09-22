# Exercício Python 19: Um professor quer sortear um dos seus quatro alunos para apagar o quadro. 
# Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

# Utilizando import random
import random
a1 = str(input('Primeiro aluno:'))
a2 = str(input('Segundo aluno:'))
a3 = str(input('Terceiro aluno:'))
a4 = str(input('Quarto aluno:'))

lista = [a1, a2, a3, a4] #quando for criar uma lista ela fica em colchetes.

escolhido = random.choice(lista) #random.choice retorna um elemento da sequência sorteada
print('O aluno escolhido foi {}' .format(escolhido))

# Utilizando from random import choice

from random import choice

a1 = str(input('Primeiro aluno:'))
a2 = str(input('Segundo aluno:'))
a3 = str(input('Terceiro aluno:'))
a4 = str(input('Quarto aluno:'))

lista = [a1, a2, a3, a4] #quando for criar uma lista ela fica em colchetes.

escolhido = choice(lista) #random.choice retorna um elemento da sequência sorteada
print('O aluno escolhido foi {}' .format(escolhido))

