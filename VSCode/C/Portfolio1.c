#include <stdio.h>
#include <stdlib.h>
#include <locale.h>

int main() {
    // declarar variáveis de entrada
    char nome_animal[30];
    int qnt_animal;
    double custo_comida;
    double qnt_comida;

    // declarar variáveis de saída
    double custo_dia;
    double qnt_comida_mes;
    double custo_mes;
    
    setlocale(LC_ALL, "portuguese");
    
    // query
    printf("Informe o nome do animal: ");
    scanf("%s", nome_animal);
    printf("Informe a Quantidade de animais: ");
    scanf("%d", &qnt_animal);  
    printf("Informe o custo de alimentação: ");
    scanf("%lf", &custo_comida);
    printf("Informe a quantidade de alimentação: ");
    scanf("%lf", &qnt_comida);

    // calculos
    custo_dia = qnt_animal * custo_comida * qnt_comida;
    qnt_comida_mes = qnt_animal * qnt_comida * 30; 
    custo_mes = custo_dia * 30;

    // resultados
    printf("Animal: %s\n", nome_animal);
    printf("Custo estimado p/dia: R$ %.2f\n", custo_dia);
    printf("Qnt de comida consumida p/mês(kg): %.2f\n", qnt_comida_mes);
    printf("Custo estimado p/mês: %.2f\n", custo_mes);

    system("pause");
    return 0;
}