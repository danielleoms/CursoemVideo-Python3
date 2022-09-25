#Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
# se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

anoAtual = date.today().year
ano = int(input('Ano de nascimento:'))
atraso = anoAtual - (ano + 18)
falta = 18 - (anoAtual - ano)
idade = anoAtual - ano
anoAlist = ano + 18

if idade == 18:
    print('Quem nasceu em {} tem {} anos.\nVocê tem que se alistar esse ano.' .format(ano, idade))

elif idade >= 18:
    print('Quem nasceu em {} tem {} anos.' .format(ano, idade))
    print('Você já deveria ter se alistado há {} anos.' .format(atraso))
    print('Seu alistamento foi em {}.' .format(anoAlist))

elif idade <= 17:
    print('Quem nasceu em {} tem {} anos.'.format(ano, idade))
    print('Faltam {} ano(s) para você se alistar.'.format(falta))
    print('Seu alistamento será em {}.'.format(anoAlist))

