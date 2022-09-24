# Exercício Python 34: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Qual é o salário do funcionário? R$'))

if salario > 1250:
    print('O salário que era de R${:.2f}, agora vai ser de R${:.2f}'.format(salario, salario + (salario * 10 / 100)))
else:
    print('O salário que era de R${:.2f}, agora vai ser de R${:.2f}' .format(salario, salario + (salario * 15 / 100)))

print('-==-' * 30)

#RESOLUÇÃO DO GUANABARA

sal = float(input('Qual é o salário do funcionário?'))

if sal <= 1250:
    novo = sal + (sal * 15 / 100)
else:
    novo = sal + (sal * 10 / 100)
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.' .format(sal, novo))
