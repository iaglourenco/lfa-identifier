# LFA Identifier


## Projeto da disciplina Linguagens Formais e Autômatos

## Descrição

 Definir uma Gramática G para uma linguagem equivalente a um subconjunto da Linguagem de Programação C, que contenha os seguintes recursos:

- Programa principal `main()`

- Delimitadores `{  }` para blocos

- Delimitador `;` de comandos

- Variáveis do tipo inteiro (nome da variável é composto apenas de letras e o seu valor por cadeia de dígitos);

- Comando de entrada simplificado: `scanf(variável)`;

- Comando de saída simplificado: `printf(variável)`;

- Comando de atribuição: ` = `;

- As expressões podem conter variáveis, valores absolutos e operadores aritméticos;

- Operadores aritméticos:` +,-,*,/ `;


### Caso Teste exemplo 1:

- Entrada:
```c
main(){
  int valora,valorb,soma,media;
  scanf(valora);
  scanf(valorb);
  soma=valora+valorb;
  media=soma/2;
  printf(media);
}
```
- Saída

    Aceita           

 

### Caso Teste exemplo 2:

- Entrada:
```c
main(){
  int valora,valorb,soma,media;
  scanf(valora);
  scanf(valorb);
  soma=valora valorb; //erro
  media=soma/2;
  printf(media);
}
```
- Saída

    Rejeitada      



## Como utilizar

- Voce vai precisar o interpretador Python 3 instalado em sua máquina;
- Com ele devidamente instalado, basta executar o arquivo `main.py` com o CLI (terminal);
- Ex. `python3 main.py <arquivo_de_entrada.txt>`

- A gramática está definida em `grammar.txt`;
- Há varios testes disponíveis em `/testes/`;  


## Autores

- Bruno Camilo - [@BrunoSilverio](http://github.com/BrunoSilverio)
- Iago Lourenço - [@iaglourenco](http://github.com/iaglourenco)