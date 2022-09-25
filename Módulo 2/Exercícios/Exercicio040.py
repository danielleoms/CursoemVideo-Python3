#Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média,
# mostrando uma mensagem no final, de acordo com a média atingida:

#– Média abaixo de 5.0: REPROVADO
#– Média entre 5.0 e 6.9: RECUPERAÇÃO
#– Média 7.0 ou superior: APROVADO

nota1 = float(input('Primeira nota:'))
nota2 = float(input('Segunda nota:'))
media = (nota1 + nota2) / 2

if media < 5.0:
    print('Sua média foi {:.1f}, ou seja insuficiente, infelizmente você está REPROVADO.' .format(media))
elif media >= 5.0 and media < 7:
    print('Sua média foi {:.1f} e você está de RECUPERAÇÃO.' .format(media))
elif media >= 7:
    print('Parabéns, sua média foi {} e você está APROVADO.' .format(media))
