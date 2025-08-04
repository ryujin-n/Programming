#include <stdio.h>
#include <locale.h>

int main() {
    int i;
    setlocale(LC_ALL, "pt_BR.UTF-8");
    
    i = 0;
    
    while (i < 21) //no WHILE, a condição é verificada antes de cada iteração (toda vez que a condiçao for verdadeira, o codigo vai rodar)
    {
        printf("anyohaseyo, isso foi impresso %d vezes\n", i);
        i++;
    }
    
    return 0;

    //ele é útil quando a gente não sabe quantas vezes o loop vai executar, tipo Leitura de arquivos até o fim, 
    //processamento de dados até uma condição ser atendida (while (valor != 0) ou jogos (game loops: while (jogoAtivo)

    //a parte ruim é que tem que tomar muito cuidado, pq é mto facil dar um loop infinito com isso daqui
}