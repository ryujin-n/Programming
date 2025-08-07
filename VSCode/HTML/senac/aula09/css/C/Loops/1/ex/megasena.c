#include <stdio.h>
#include <stdlib.h>
#include <locale.h>
#include <time.h>

int main() {
    
    setlocale(LC_ALL, "pt_BR.UTF-8");

    int i = 0;
    int num;
    srand(time(NULL));

    printf("Números para MegaSena :DD!!!! \n");
    while (i <=6)
    {
        num = 1 + rand()%60;
        printf("%d ",num);
        i++;
    }
    printf("\n");
    
    return 0;
}