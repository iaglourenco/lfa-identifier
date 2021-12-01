# LFA Identifier
# Authors
# - Bruno Camilo - @BrunoSilverio
# - Iago Lourenço - @iaglourenco
# Objetivo:
# - Dado um arquivo de entrada contendo um código em C, validar se a sintaxe é válida.
# - Para mais informações, veja README.md

import sys
import re

reserved_words = [
    "main()",
    ";",
    "printf(",
    "scanf(",
    "=",
    "+",
    "-",
    "*",
    "/",
    "int ",
    "{",
    "}",
    "(",
    ")",
]

# Vetor para guardar as variaveis já declaradas
declared_vars = []


def monta_simbolo(input: str):
    # Função que caso o input seja uma palavra reservada, retorna o simbolo correspondente
    word = ""

    for caracter in input:
        word += caracter
        if word in reserved_words:
            return word
    return None


def valida_variavel(input: str):
    # Função para verificar declaração de variaveis
    # Verifica se o nome de variavel é valido, retorna True ou False

    word = ""
    vars = ""

    if not input[0].isalpha():  # Verifica se o primeiro caracter é uma letra
        return False  # Se não for, retorna False

    for character in input:
        if word + "(" in reserved_words and len(word) > 0:
            return (
                False  # Se o nome da variavel for uma palavra reservada, retorna False
            )

        if character.isalpha():  # Se for letra
            word += character  # Adiciona o caracter ao nome da variavel
            continue  # Continua

        if character == ",":  # Se for virgula
            vars += (
                word + character
            )  # Adiciona o nome da variavel a string de variaveis
            word = ""
            continue

        # Se for ponto e virgula termina a detecção e o ultimo caracter não foi virgula
        if character == ";":
            vars += (
                word + character
            )  # Adiciona o nome da variavel a string de variaveis
            if vars[-2] != ",":
                # Substitui as variaveis reconhecidas da entrada
                input = input.replace(vars + character, "")
                # Adiciona as variaveis ao vetor de variaveis
                declared_vars.extend(vars.replace(";", "").split(","))

                return vars

        else:
            return False  # Se não, retorna False


def valida_variavel_declarada(input: str):
    # Função para validar se as variaveis do scanf, printf  foram declaradas anteriormente
    # assim validando se o nome é válido
    if input in declared_vars:
        return input
    else:
        return False


def valida_variavel_declarada_e_numero(input: str):
    # Função para validar se as variaveis foram declaradas anteriormente ignorando numeros
    # Exemplo: input = "<nome>,9" somente o <nome> será validado
    # A entrada consiste de duas partes separadas por virgula onde a vírgula é anteriormente o operador
    # Usada para validar estruturas de atribuição

    for var in input.split(","):
        if var.strip() in declared_vars or var.strip().isdigit():
            continue
        else:
            return False
    return input


def erro(onde: str):
    print("Rejeitada", onde)
    sys.exit(-1)


# Programa principal
if __name__ == "__main__":
    # Verifica se o número de argumentos é igual a 2
    if len(sys.argv) != 2:
        print("Usage: ./main.py <input>")
        sys.exit(1)

    # Abre o arquivo de entrada
    with open(sys.argv[1], "r") as f:
        input = f.read().strip()

    # Exibo o conteúdo do arquivo de entrada
    print(input)

    # Remoção de quebras de linha, tabulação e espaços
    input = input.replace("\n", "").replace("\t", "").strip()

    # Inicio da validação sintática, quando o simbolo é devidamente é reconhecido o mesmo é removido da entrada, deixando somente o restante da entrada

    # Valida o simbolo "main()"
    simbolo = monta_simbolo(input).strip()
    if simbolo != "main()":
        erro("ERRO: main")
    # Caso o simbolo tenha sido corretamente reconhecido, remove-o da entrada (esse passo é repetido em todas as identificações posteriores)
    input = input.replace(simbolo, "", 1).strip()
    # ----------------------------------------------------

    # Valida o simbolo"{"
    simbolo = monta_simbolo(input)
    if simbolo != "{":
        erro("ERRO: {")
    input = input.replace(simbolo, "", 1).strip()

    # Enquanto houver conteúdo na entrada
    while len(input):

        simbolo = monta_simbolo(input)
        # ----------------------------------------------------
        # Valida "}"
        if simbolo == "}":
            input = input.replace(simbolo, "", 1).strip()
            if len(input) > 0:
                erro("Algo fora do colchete")
            else:
                print("Aceita")
                break
        # ----------------------------------------------------
        # Valida <decl vars>
        elif simbolo == "int ":
            simbolo = monta_simbolo(input)
            if simbolo != "int ":
                erro("ERRO: declaração de variaveis")
            input = input.replace(simbolo, "", 1).strip()
            # Valida <nome_variaveis>
            simbolo = valida_variavel(input)
            if not simbolo:
                erro("ERRO: nome de variavel")
            input = input.replace(simbolo, "", 1).strip()
        # ----------------------------------------------------
        # Valida <scanf>
        elif simbolo == "scanf(":
            simbolo = monta_simbolo(input)
            if simbolo != "scanf(":
                erro("ERRO: scanf")
            input = input.replace(simbolo, "", 1).strip()
            # Chama função para validação do nome da variavel
            simbolo = valida_variavel_declarada(input.split(")", 1)[0])
            if not simbolo:
                erro("ERRO: variavel parametro scanf")
            input = input.replace(simbolo, "", 1).strip()

            # Valida fechamento do scanf ")"
            simbolo = monta_simbolo(input)
            if simbolo != ")":
                erro("ERRO: )")
            input = input.replace(simbolo, "", 1).strip()
            # Valida fechamento do scanf ";"
            simbolo = monta_simbolo(input)
            if simbolo != ";":
                erro("ERRO: ;")
            input = input.replace(simbolo, "", 1).strip()
        # ----------------------------------------------------
        # Valida <printf>
        elif simbolo == "printf(":
            simbolo = monta_simbolo(input)
            if simbolo != "printf(":
                erro("ERRO: printf")
            input = input.replace(simbolo, "", 1).strip()
            # Chama função para validação do nome da variavel
            simbolo = valida_variavel_declarada(input.split(")", 1)[0])
            if not simbolo:
                erro("ERRO: variavel parametro printf")
            input = input.replace(simbolo, "", 1).strip()

            # Valida fechamento do printf ")"
            simbolo = monta_simbolo(input)
            if simbolo != ")":
                erro("ERRO: )")
            input = input.replace(simbolo, "", 1).strip()
            # Valida fechamento do printf ";"
            simbolo = monta_simbolo(input)
            if simbolo != ";":
                erro("ERRO: ;")
            input = input.replace(simbolo, "", 1).strip()
        # ----------------------------------------------------
        # Valida <Atribuição>
        elif valida_variavel_declarada(input.split("=", 1)[0]):
            variavel_operacao = valida_variavel_declarada(
                input.split("=", 1)[0])
            input = input.replace(variavel_operacao + "=", "", 1).strip()

            # Substitui do input os caracteres '+', '-', '*', '/' por vírgula
            # Pois para a sintaxe a ordem não importa
            input = input.replace("+", ",").strip()
            input = input.replace("-", ",").strip()
            input = input.replace("*", ",").strip()
            input = input.replace("/", ",").strip()
            operacao_vars = valida_variavel_declarada_e_numero(
                input.split(";", 1)[0])
            if operacao_vars:
                input = input.replace(input.split(";", 1)[0], "").strip()

                # Valida fechamento da operacao ";"
                simbolo = monta_simbolo(input)
                if simbolo != ";":
                    erro("ERRO: ;")
                input = input.replace(simbolo, "", 1).strip()

            else:
                erro("ERRO: Equacao")

        # ----------------------------------------------------
        else:
            erro("Instrução estranha")
