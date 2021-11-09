# LFA Identifier
# Authors
# - Bruno Camilo - @BrunoSilverio
# - Iago Lourenço - @iaglourenco

import sys

reserved_words = [
    'main',
    ';',
    'printf',
    'scanf',
    '=',
    '+',
    '-',
    '*',
    '/',
    'int' 
]

# Variável de armazenamento de possíveis erros encontrados (linha/causa)
str_err = "" 

# Função que itera sobre a string de entrada e retorna o próprio @input caso seja válido ou a palavra reservada correspondente, ou @None caso nenhuma das opções seja válida
def monta_simbolo(input: str):

    return

# Função que verifica se o nome de variavel é valido, retorna True ou False
def valida_variavel(input: str):
    return


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: ./main.py <input>')
        exit(1)
    
    with open(sys.argv[1], 'r') as f:
        input = f.read().strip()
    
    print(input)
    while len(input) > 0:  
        simbolo = monta_simbolo(input)