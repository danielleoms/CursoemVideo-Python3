#Exercício Python 14: Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

#A equação é °F = (°C x 1,8) + 32. Você também pode usar a fórmula °F = °C x 9 ÷ 5 + 32

celcius = float(input('Informe a temperatura em C:'))
fahrenheit =  (celcius * 9 ) / 5 + 32

print('A temperatura de {:.2f}ºC corresponde a {:.2f}ºF.' .format(celcius,fahrenheit))
