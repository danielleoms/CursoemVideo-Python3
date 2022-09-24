#Exercício Python 28: Escreva um programa que faça o computador “pensar”
# em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.

import random

lista = [0, 1, 2, 3, 4, 5]
escolhido = random.choice(lista) #choice retorna um elemento da sequência sorteada
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
chute = int(input('Qual número você acha que o computador sorteou?'))

if chute == escolhido:
    print('Parabéns você acertou!O número sorteado pelo computador foi {}.' .format(escolhido))

else:
    print('Poxa, você errou!O número sorteado pelo computador foi {}.' .format(escolhido))


#RESOLUÇÃO DO GUANABARA:
#Função RANDINT serve para solucionar, de forma aleatória, um número inteiro, dentro de valores passados pelo usuário.

from time import sleep #Número de segundos durante os quais o código deve ser interrompido.
computador = random.randint(0, 5)
print(' -=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei?'))
print('PROCESSANDO...')
sleep(3)

if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI!Eu pensei no número {} e não no {}!' .format(computador, jogador))
