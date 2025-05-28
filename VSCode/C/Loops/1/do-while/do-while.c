#include <stdio.h>
#include <stdlib.h>
#include <locale.h>

int main() {
    
    int i;
    
    setlocale(LC_ALL, "pt_BR.UTF-8");

    i=0;
    
    do //no DO WHILE o codigo é executado antes de verificar a condição
    {
        printf("hii, isso foi impresso %d vezes \n",i);
        i++;
    } while (i <= 20);

    
    return 0;

    //ele é ideal pra para situações onde a primeira execução é obrigatória, tipo menus interativos, validação de entrada do usuário
    //ou processos que precisam rodar pelo menos uma vez (gerar um número aleatório até ser válido)
}