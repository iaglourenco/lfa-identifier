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



## Autores

- Bruno Camilo - [@BrunoSilverio](http://github.com/BrunoSilverio)
- Iago Lourenço - [@iaglourenco](http://github.com/iaglourenco)