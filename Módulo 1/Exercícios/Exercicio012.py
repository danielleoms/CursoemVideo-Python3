#Exercício Python 12: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

#OBS: Para calcular porcentagem de desconto basta você pegar o valor sem desconto (V) do produto e multiplicar pela porcentagem (%).
# Para obter o valor final com desconto (Vf), pegue o valor sem desconto (V) e subtraia pelo resultado da conta anterior, que é o valor descontado (Vd).

produto = float(input('Qual é o preço do produto? R$'))
vd = produto * 0.05
vf = produto - vd

print('O produto que custava R${}, na promoção com desconto de 5% vai custar R${}.' .format(produto,vf))

#resolução do guanabara:

produto = float(input('Qual é o preço do produto?R$'))
novo = produto - (produto * 5 / 100)
print('O produto que custava R${}, na promoção com desconto de 5% vai custar R${}.' .format(produto,novo))
