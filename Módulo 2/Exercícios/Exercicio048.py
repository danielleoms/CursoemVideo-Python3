#Exercício Python 48: Faça um programa que calcule a soma entre todos os números ímpares
# que são múltiplos de três e que se encontram no intervalo de 1 até 500.

#Minha resolução
s=0
for c in range(1, 501):
    if c % 3 ==0 and c % 2 != 0:
        print(c, end=' ')
    s += c
print('A soma dos múltiplos de três e que se encontram no intervalo de 1 até 500 é: {}.' .format(s))

#Resolução do guanabara
cont = 0
soma = 0
for c in range(1, 501,2):
    if c % 3 == 0:
        soma = soma + c
        cont = cont + 1
print('A soma de todos os {} valores solicitados é {}.' .format(cont, soma))
