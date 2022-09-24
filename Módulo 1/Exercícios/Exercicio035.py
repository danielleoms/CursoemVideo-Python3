#Exercício Python 35: Desenvolva um programa que leia o comprimento de três retas
# e diga ao usuário se elas podem ou não formar um triângulo.
# (Obs.: Para formar um triângulo, cada suposto lado deve ser menor do que a soma dos outros dois lados.)

print('-=-' * 30)
print('ANALISADOR DE TRIÂNGULOS')
print('-=-' * 30)

a = float(input('Primeiro segmento:'))
b = float(input('Segundo segmento:'))
c = float(input('Terceiro segmento:'))

if a < b + c and b < c + a and c < b + a:
    print('Os seguimentos acima podem formar um triângulo e seu perimêtro é {}.' .format(a+b+c))
else:
    print('Os seguimentos acima não podem forma um triângulo.')
