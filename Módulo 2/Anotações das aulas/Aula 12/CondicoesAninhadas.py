#Aula 12 – Condições Aninhadas
#pode usar dentro do if inúmeras elif,

"""Exemplo de Estrutura Condicional Aninhada:
if <CONDIÇÃO 1>:
    <COMANDOS A>
elif <CONDIÇÃO 2>:
    <COMANDOS B>
elif <CONDIÇÃO 3>:
    <COMANDOS C>
else:
    <COMANDOS D>"""


nome = str(input('Qual é o seu nome?'))
if nome == 'Gustavo':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Cláudia Jéssica Juliana': #usar o in no lugar do ==
    print('Belo nome feminino')
else:
    print('Seu nome é bem normal!')
print('Tenha um bom dia, {}!'.format(nome))
