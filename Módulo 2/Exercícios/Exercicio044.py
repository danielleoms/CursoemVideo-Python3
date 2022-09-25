"""
Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

– à vista dinheiro/cheque: 10% de desconto

– à vista no cartão: 5% de desconto

– em até 2x no cartão: preço formal

– 3x ou mais no cartão: 20% de juros
"""

print('{:=^40}' .format(' LOJAS GUANABARA '))

num1 = float(input('Qual o valor do produto? R$ '))

print('-=-' * 10)

print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque: 10% de desconto
[ 2 ] à vista no cartão: 5% de desconto
[ 3 ] em até 2x no cartão: preço formal
[ 4 ] 3x no cartão ou mais: 20% de juros''')
opcao = int(input('Sua opção:'))

if opcao == 1:
    print('''O valor do produto era de R${}, no pagamento à vista com dinheiro/cheque tem desconto de 10%:
Agora o valor é R$ {:.2f}.''' .format(num1, (num1 - (num1 * 10/100))))
if opcao == 2:
    print('''O valor do produto era de R${}, no pagamento à vista no cartão tem desconto de 5%:
Agora o valor é R$ {:.2f}.'''.format(num1, (num1 - (num1 * 5 / 100))))
if opcao == 3:
    print('Nessa opção de pagamento não existe desconto, o valor do produto de R${} vai ser dividido em duas vezes de R${:.2f}.'.format(num1, num1 / 2))
if opcao == 4:
    print('O valor do produto era de R${}, no pagamento em 3x ou mais, existe um acréscimo de 20% de juros no valor do produto R${:.2f}.' .format(num1, (num1 + (num1 * 20 / 100))))

#RESOLUÇÃO DO GUANABARA 

"""
EXERCÍCIO 044: Gerenciador de Pagamentos
Elabore um programa que calcule o valor a ser pago de um produto,
considerando o seu preço normal, e condição de pagamento:
- À vista no dinheiro/cheque: 10% de desconto
- À vista no cartão: 5% de desconto
- Em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros
"""
print('{:=^40}'.format(' LOJAS GUANABARA '))
preco = float(input('Preço das compras: R$ '))
print('''FORMAS DE PAGAMENTO
[ 1 ] À vista no dinheiro/cheque
[ 2 ] À vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opcao = int(input('Qual é a opção? '))
if opcao == 1:
    total = preco - (preco * 10 / 100)
elif opcao == 2:
    total = preco - (preco * 5 / 100)
elif opcao == 3:
    total = preco
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R$ {:.2f} SEM JUROS.'.format(parcela))
elif opcao == 4:
    total = preco + (preco * 20 / 100)
    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc
    print('Sua compra será parcelada em {}x de R$ {:.2f} COM JUROS.'.format(totparc, parcela))
else:
    total = preco
    print('OPÇÃO INVÁLIDA de pagamento. Tente novamente!')
print('Sua compra de R$ {:.2f} vai custar R$ {:.2f} no final.'.format(preco, total)
