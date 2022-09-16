#Exercício Python 15: Escreva um programa que pergunte a quantidade de Km percorridos
# por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

dias = int(input('Por quantos dias você alugou o carro?' ))
km = float(input('Quantos km rodados?' ))
preço = (0.15 * km) + (60 * dias)

print('Você terá que pagar R${:.2f}, por ter usado o carro por {} dias e {}km rodados.' .format(preço,dias,km))
