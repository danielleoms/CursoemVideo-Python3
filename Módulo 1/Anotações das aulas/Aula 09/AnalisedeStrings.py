frase = 'Curso em Vídeo Python'

print(len(frase))  # Quantidade de caracteres de uma string, no caso, 21

print(frase.count('o')) # Quantidade de vezes que o caractere entre parênteses "o" aparece na string 

print(frase.count('o', 0, 13)) # Foi incluído um fatiamento do índice [0] ao [13], exibindo somento um "o"

print(frase.count('o', 0, 14))  # O índice final ficou sendo [14], exibindo dois "o"

print(frase.find('deo'))  # Procura DEO na frase e indica em que momento começou [11]

print(frase.find('Android'))  # Quando se procura na string algo que não está presente, o valor exibido é "-1"

print('Curso' in frase)  # Verifica se o que está entre aspas está presente na string, e se sim, exibe "True"

"""
[C] [u] [r] [s] [o] [ ] [e] [m] [ ] [V] [í ] [d ] [e ] [o ] [  ] [P ] [y ] [t ] [h ] [o ] [n ]
[0] [1] [2] [3] [4] [5] [6] [7] [8] [9] [10] [11] [12] [13] [14] [15] [16] [17] [18] [19] [20]
"""
