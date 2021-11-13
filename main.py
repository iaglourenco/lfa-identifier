# LFA Identifier
# Authors
# - Bruno Camilo - @BrunoSilverio
# - Iago Lourenço - @iaglourenco

import sys

reserved_words = [
    'main()',
    ';',
    'printf',
    'scanf',
    '=',
    '+',
    '-',
    '*',
    '/',
    'int ',
    '{',
    '}',
    '(',
    ')'
]


def monta_simbolo(input: str):
    word = ''

    for caracter in input:
        word += caracter
        if caracter in reserved_words:
            return word
    return None

# <main>::= main() { <decl vars> <comandos> }
# main(){   int valora,valorb,soma,media;   scanf(valora);   scanf(valorb);   soma=valora+valorb;    media =soma/2;   printf(media);}

# Função para verificar declaração de variaveis
# Verifica se o nome de variavel é valido, retorna True ou False
# int valora,valorb,soma,media;


def valida_variavel(input: str):
    word = ''
    if not input[0].isalpha():  # Verifica se o primeiro caracter é uma letra
        return False  # Se não for, retorna False

    for character in input:
        word += character   # Adiciona o caracter ao nome da variavel

        if character.isalpha():  # Se for letra
            continue             # Continua

        if character == ',':  # Se for virgula
            input.replace(word, '')  # Remove a palavra da string
            if character.isalpha():  # Após a virgula, se for letra
                continue  # Continua o loop
            else:
                return False  # Se não for letra, retorna False

        if character == ';':  # Se for ponto e virgula termina a detecção
            return input  # Retorna a string

        return False  # Se não for nenhum dos casos acima, retorna False


# Função que valida equações aka. (s=a+b)
def valida_operacao(input: str):

    return True


def deuruim():
    print('Rejeitada')
    exit(-1)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: ./main.py <input>')
        exit(1)

    with open(sys.argv[1], 'r') as f:
        input = f.read().strip()

    print(input)
    while len(input):
        # Valida "main()"
        simbolo = monta_simbolo(input)
        if simbolo != "main()":
            deuruim()

        # Valida "{"
        input.replace(simbolo, '')
        simbolo = monta_simbolo(input)
        if simbolo != '{':
            deuruim()

        # Valida <decl vars>
        input.replace(simbolo, '')
        simbolo = monta_simbolo(input)
        if simbolo != 'int ':
            deuruim()

        # Valida <nome_variaveis>
        input.replace(simbolo, '')
        input = valida_variavel(input)
        if input is False:
            deuruim()
