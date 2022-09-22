"""
EXERCÍCIO 027: Primeiro e Último Nome de uma Pessoa
Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro
e o último nome separadamente.
Ex: Danielle Oliveira Moreno de Souza
Primeiro = Danielle
Último = Souza
"""

n = str(input('Digite seu nome completo: ')).strip() #função strip tira os espaços desnecesários
nome = n.split() #função slip transforma em lista
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}.'.format(nome[0]))
print('Seu último nome é {}.'.format(nome[len(nome) - 1]))
