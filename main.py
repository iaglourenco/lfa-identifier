# LFA Identifier
# Authors
# - Bruno Camilo - @BrunoSilverio
# - Iago Lourenço - @iaglourenco

import sys
import re
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
        if word+'(' in reserved_words and len(word) > 0:
            return False  # Se o nome da variavel for uma palavra reservada, retorna False

        if character.isalpha():  # Se for letra
            word += character   # Adiciona o caracter ao nome da variavel
            continue            # Continua

        if character == ',':  # Se for virgula
            vars += word+character  # Adiciona o nome da variavel a string de variaveis
            word = ''
            continue

        # Se for ponto e virgula termina a detecção e o ultimo caracter não foi virgula
        if character == ';':
            vars += word+character  # Adiciona o nome da variavel a string de variaveis
            if vars[-2] != ',':
                # Substitui as variaveis reconhecidas da entrada
                input = input.replace(vars+character, '')
                # Adiciona as variaveis ao vetor de variaveis
                declared_vars.extend(vars.replace(";", "").split(','))

                return vars

        else:
            return False  # Se não, retorna False


def valida_variavel_declarada(input: str):
    # Função para validar se as variaveis do scanf, printf  foram declaradas anteriormente
    if input in declared_vars:
        return input
    else:
        return False


def valida_variavel_declarada_e_numero(input: str):
    # Função para validar se as variaveis foram declaradas anteriormente ignorando numeros

    for var in input.split(','):
        if var.strip() in declared_vars or var.strip().isdigit():
            continue
        else:
            return False
    return input


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
    # Valida "main()"
    simbolo = monta_simbolo(input).strip()
    if simbolo != "main()":
        deuruim("main")
    input = input.replace(simbolo, '', 1).strip()
    # ----------------------------------------------------
    # Valida "{"
    simbolo = monta_simbolo(input)
    if simbolo != '{':
        deuruim("{")
    input = input.replace(simbolo, '', 1).strip()

    while len(input):

        simbolo = monta_simbolo(input)
        # ----------------------------------------------------
        # Valida "}"
        if simbolo == '}':
            input = input.replace(simbolo, '', 1).strip()
            if len(input) > 0:
                deuruim("Algo fora do colchete")
            else:
                print("Aceita")
                break
        # ----------------------------------------------------
        # Valida <decl vars>
        elif(simbolo == 'int '):
            simbolo = monta_simbolo(input)
            if simbolo != 'int ':
                deuruim("decl vars")
            input = input.replace(simbolo, '', 1).strip()
            # Valida <nome_variaveis>
            simbolo = valida_variavel(input)
            if not simbolo:
                deuruim("name vars")
            input = input.replace(simbolo, '', 1).strip()
        # ----------------------------------------------------
        # Valida <scanf>
        elif(simbolo == 'scanf('):
            simbolo = monta_simbolo(input)
            if simbolo != 'scanf(':
                deuruim("scanf")
            input = input.replace(simbolo, '', 1).strip()
            # Chama função valida variavel
            simbolo = valida_variavel_declarada(input.split(')', 1)[0])
            if not simbolo:
                deuruim("scanf var")
            input = input.replace(simbolo, '', 1).strip()

            # Valida fechamento do scanf ")"
            simbolo = monta_simbolo(input)
            if simbolo != ')':
                deuruim(")")
            input = input.replace(simbolo, '', 1).strip()
            # Valida fechamento do scanf ";"
            simbolo = monta_simbolo(input)
            if simbolo != ';':
                deuruim(";")
            input = input.replace(simbolo, '', 1).strip()
        # ----------------------------------------------------
        # Valida <printf>
        elif(simbolo == 'printf('):
            simbolo = monta_simbolo(input)
            if simbolo != 'printf(':
                deuruim("printf")
            input = input.replace(simbolo, '', 1).strip()
            # Chama função valida variavel
            simbolo = valida_variavel_declarada(input.split(')', 1)[0])
            if not simbolo:
                deuruim("printf var")
            input = input.replace(simbolo, '', 1).strip()

            # Valida fechamento do printf ")"
            simbolo = monta_simbolo(input)
            if simbolo != ')':
                deuruim(")")
            input = input.replace(simbolo, '', 1).strip()
            # Valida fechamento do printf ";"
            simbolo = monta_simbolo(input)
            if simbolo != ';':
                deuruim(";")
            input = input.replace(simbolo, '', 1).strip()
        # ----------------------------------------------------
        # Valida <Operadores>
        elif valida_variavel_declarada(input.split('=', 1)[0]):
            variavel_operacao = valida_variavel_declarada(
                input.split('=', 1)[0])
            input = input.replace(variavel_operacao+'=', '', 1).strip()

            # Substitui do input os caracteres '+', '-', '*', '/'
            input = input.replace('+', ',').strip()
            input = input.replace('-', ',').strip()
            input = input.replace('*', ',').strip()
            input = input.replace('/', ',').strip()
            operacao_vars = valida_variavel_declarada_e_numero(
                input.split(";", 1)[0])
            if operacao_vars:
                input = input.replace(input.split(";", 1)[0], '').strip()

             # Valida fechamento da operacao ";"
                simbolo = monta_simbolo(input)
                if simbolo != ';':
                    deuruim(";")
                input = input.replace(simbolo, '', 1).strip()

            else:
                deuruim("Equacao var")

            # media=soma/2;
            # soma/valora;
            # soma,2
            # ["soma"  "2"]
            # isAlpha -> validar variavel
            # else numero

        # ----------------------------------------------------
        else:
            deuruim("Instrução estranha")
