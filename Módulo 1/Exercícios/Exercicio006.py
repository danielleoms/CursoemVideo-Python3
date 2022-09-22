#EXERCÍCIO 006: Dobro, Triplo, Raiz Quadrada
#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n = int(input('Digite um número:'))
d = n * 2
t = n * 3
r = n ** (1/2)

print('O dobro de {} vale {}' .format(n, d))
print('O triplo de {} vale {}, e a raiz quadrada vale {:.3f}.' .format(n,t,r))
