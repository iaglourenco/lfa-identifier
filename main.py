# LFA Identifier
# Authors
# - Bruno Camilo - @BrunoSilverio
# - Iago Lourenço - @iaglourenco

import sys

reserved_words = [
    'main()',
    ';',
    'printf(',
    'scanf(',
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

# Vetor para guardar as variaveis
declared_vars = []


def monta_simbolo(input: str):
    word = ''

    for caracter in input:
        word += caracter
        if word in reserved_words:
            return word
    return None

# <main>::= main() { <decl vars> <comandos> }
# main(){   int valora,valorb,soma,media;   scanf(valora);   scanf(valorb);   soma=valora+valorb;    media =soma/2;   printf(media);}


def valida_variavel(input: str):
    # Função para verificar declaração de variaveis
    # Verifica se o nome de variavel é valido, retorna True ou False

    word = ''
    vars = ''

    if not input[0].isalpha():  # Verifica se o primeiro caracter é uma letra
        return False  # Se não for, retorna False

    for character in input:

        if character.isalpha():  # Se for letra
            word += character   # Adiciona o caracter ao nome da variavel
            continue            # Continua

        if character == ',':  # Se for virgula
            vars += word+character  # Adiciona o nome da variavel a string de variaveis
            word = ''
            continue

        # Se for ponto e virgula termina a detecção e o ultimo caracter não foi virgula
        if vars[-1] != ',' and character == ';':
            vars += word+character  # Adiciona o nome da variavel a string de variaveis
            # Substitui as variaveis reconhecidas da entrada
            input = input.replace(vars+character, '')
            # Adiciona as variaveis ao vetor de variaveis
            declared_vars.append(vars.replace(";", "").split(','))
            return True

        else:
            return False  # Se não, retorna False


def valida_variavel_declarada(input: str):
    # Função para validar se as variaveis do scanf, printf e operações foram declaradas anteriormente
    var = ''
    for character in input:
        var += character
        if var in declared_vars:
            return True


def valida_operacao(input: str):
    # Função que valida equações aka. (s=a+b

    return True


def deuruim(onde: str):
    print('Rejeitada', onde)
    exit(-1)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: ./main.py <input>')
        exit(1)

    with open(sys.argv[1], 'r') as f:
        input = f.read().strip()

    print(input)
    input = input.replace("\n", "").replace("\t", "").strip()
    while len(input):
        # Valida "main()"
        simbolo = monta_simbolo(input).strip()
        if simbolo != "main()":
            deuruim("main")
        input = input.replace(simbolo, "").strip()
        # ----------------------------------------------------
        # Valida "{"
        simbolo = monta_simbolo(input)
        if simbolo != '{':
            deuruim("{")
        input = input.replace(simbolo, '').strip()
        # ----------------------------------------------------
        # Valida <decl vars>
        simbolo = monta_simbolo(input)
        if simbolo != 'int ':
            deuruim("decl vars")
        input = input.replace(simbolo, '').strip()
        # ----------------------------------------------------
        # Valida <nome_variaveis>
        if not valida_variavel(input):
            deuruim("name vars")
        input = input.replace(simbolo, '').strip()
        # ----------------------------------------------------
        # Valida <scanf>
        simbolo = monta_simbolo(input)
        if simbolo != 'scanf(':
            deuruim("scanf")
        input = input.replace(simbolo, '').strip()
        # Chama função valida variavel

        # Valida fechamento do scanf ")"
        simbolo = monta_simbolo(input)
        if simbolo != ')':
            deuruim(")")
        input = input.replace(simbolo, '').strip()
        # Valida fechamento do scanf ";"
        simbolo = monta_simbolo(input)
        if simbolo != ';':
            deuruim(";")
        input = input.replace(simbolo, '').strip()
        # ----------------------------------------------------
        # Valida <printf>
        simbolo = monta_simbolo(input)
        if simbolo != 'printf(':
            deuruim("printf")
        input = input.replace(simbolo, '').strip()
        # Chama função valida variavel

        # Valida fechamento do printf ")"
        simbolo = monta_simbolo(input)
        if simbolo != ')':
            deuruim(")")
        input = input.replace(simbolo, '').strip()
        # Valida fechamento do printf ";"
        simbolo = monta_simbolo(input)
        if simbolo != ';':
            deuruim(";")
        input = input.replace(simbolo, '').strip()
        # ----------------------------------------------------
        # Valida <Operadores>

        # ----------------------------------------------------
        # Valida "}"
        simbolo = monta_simbolo(input)
        if simbolo != '}':
            deuruim("}")
        input = input.replace(simbolo, '').strip()
        # ----------------------------------------------------
