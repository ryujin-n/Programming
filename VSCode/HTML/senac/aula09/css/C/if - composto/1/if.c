#include <stdio.h>  //identificando as bibliotecas pra fazer o codigo funcionar, sem isso nada funciona
#include <stdlib.h>
#include <locale.h>

    int main()
    {
        int N1,resto; //declaração de variáveis (N1 e resto são numeros inteiros)

        setlocale(LC_ALL,"pt-br");//isso daqui é pro console identificar acentos e ç, pode ser "portuguese" ou "pt-br"

        printf("Insira N1: "); //aqui é como se o programa estivesse fazendo uma pergunta pro usuario 
        scanf("%d",&N1 ); //aqui é o programa colocando o valor q o usuario colocou dentro da variavel, %d é o indicador do tipo de variavel (inteiro)

        resto = N1 % 2; //aqui a gent ta impondo q a variavel "resto" é o resto da divisão do numero dado pelo usuario por 2 (ex: 4 dividido por 2, o resto é 2, ent a variavel "resto" vai ser igual a 2) 
        if (resto != 0)//aqui é uma condicional, basicamente ele tá verificando se a variavel resto é diferente de 0, se sim,ele vai fazre o codigo dentro do escopo
        {
            printf("N1 é Impar!");
        }
        else{ //caso o contrario, ele vai fazer esse codigo
            printf("N1 é Par!");
        }
        

        system("pause");//fim do codigo
        return 0;
    }

    
