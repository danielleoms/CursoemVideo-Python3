#Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
#Considerando 18 anos como maior de idade

from datetime import date
atual = date.today().year
qtdmaior = 0
qtdmenor = 0

for pess in range(1, 8):
    nasc = int(input('Em que ano a {}º nasceu? ' .format(pess)))
    idade = atual - nasc
    if idade >= 18:
        qtdmaior += 1
    else:
        qtdmenor += 1
print('Ao todo tivemos {} pessoas menores de idade.' .format(qtdmenor))
print('Ao todo tivemos {} pessoas maiores de idade.' .format(qtdmaior))
