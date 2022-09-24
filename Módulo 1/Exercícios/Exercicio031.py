#Exercício Python 31: Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

dist = float(input('Qual é a distância da sua viagem? '))
preço1 = 200 * 0.50
preço2 = dist * 0.45

print('Você está prestes a começar uma viagem de {:.2f}KM.' .format(dist))

if dist <= 200:
    print('E o preço de sua viagem será de R$ {:.2f}' .format(preço1))

else:
    print('E o preço de sua viagem será de R$ {:.2f}' .format(preço2))

#RESOLUÇÃO DO GUANABARA

dist = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {:.2f}KM.' .format(dist))

if dist <= 200:
    preço = dist * 0.50
else:
    preço = dist * 0.45
print('E o preço de sua passsagem será de R${:.2f}' .format(preço))
