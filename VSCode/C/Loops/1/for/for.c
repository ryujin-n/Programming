#include <stdio.h>
#include <stdlib.h>
#include <locale.h>

int main() {
    
    setlocale(LC_ALL, "pt_BR.UTF-8");
    
    for (int i = 0; i < 21; i++) // o for é uma das estruturas de repetição com condicional
                                // dentro dele a gente determina a nossa variável, a condiçao q ela deve ter e o incremento (i++), 
                               // pois a cada vez q o codigo rodar, ele deve aumentar um numero, se nn vai virar um loop infinito 
                              // e o pc vai explodir

    {
        printf("hallo, isso foi impresso %d vezes \n",i); //aqui é o codigo q deve ser feito enquanto a condição do for é verdadeira
    }

    return 0;

    // o bom dele é que toda a lógica do loop (inicialização, condição e incremento) fica em uma linha, geralmente é usado pra iterações em arrays
}