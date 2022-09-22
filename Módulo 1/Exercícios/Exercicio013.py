#Exercício Python 13: Faça um algoritmo que leia o
#salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Qual é o salário do funcionário? R$'))
nv = salario + (salario * 15/100)

print('O salário do funcionário era de R${:.2f}, com o reajuste de 15% de aumento agora é de R${:.2f}.' .format(salario,nv))


