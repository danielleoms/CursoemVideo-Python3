#Exercício Python 32: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
#Ano bissexto é divisível por 4 e não é divisível por 100.

from datetime import date
ano = int(input('Qual o ano que você quer analisar? Se for o ano atual digite 0: '))

if ano == 0:
    ano = date.today().year #vai pegar o ano atual configurado na máquina
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O {} é bissexto.'.format(ano))
else:
    print('O {} NÃO é bissexto.' .format(ano))
