#Exercício Python 51: Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.

primeiro = int(input('Primeiro termo:'))
razão = int(input('Razão:'))

#fórmula do N-ésimo termo:
décimo = primeiro + (10 - 1) * razão #colocou o dez pq ele quer o décimo termo
for c in range(primeiro, décimo + razão, razão):
    print('{}' .format(c), end=' ➞ ')
print('ACABOU')
