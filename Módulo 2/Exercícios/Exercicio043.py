"""Exercício Python 43: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, c
alcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:

– IMC abaixo de 18,5: Abaixo do Peso

– Entre 18,5 e 25: Peso Ideal

– 25 até 30: Sobrepeso

– 30 até 40: Obesidade

– Acima de 40: Obesidade Mórbida"""

peso = float(input('Qual é o seu peso? (Kg)'))
altura = float(input('Qual sua altura? (m)'))
imc = peso / (altura ** 2)

if imc < 18.5:
    print('Seu IMC é {:.2f} e você está abaixo do peso.' .format(imc))

elif imc >= 18.5 and imc < 25:
    print('Seu IMC é {:.2f} e você está no peso ideal.' .format(imc))

elif imc >= 25 and imc < 30:
    print('Seu IMC é {:.2f} e você está no sobrepeso.' .format(imc))

elif imc >= 30 and imc < 40:
    print('Seu IMC é {:.2f} e você está no obesidade.'.format(imc))

elif imc >= 40:
    print('Seu IMC é {:.2f} e você está com obesidade mórbida.'.format(imc))
