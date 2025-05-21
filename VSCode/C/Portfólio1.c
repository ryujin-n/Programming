#include <stdio.h>
#include <stdlib.h>
#include <locale.h>

int main() {
    char nome_animal[30];
    int qnt_animal;
    double custo_comida;
    double qnt_comida;
    double custo_dia;
    double qnt_comida_mes;
    double custo_mes;

    setlocale(LC_ALL, "portuguese");  

    printf("Informe o nome do animal: ");
    scanf("%29s", nome_animal);  

    printf("Informe a Quantidade de animais: ");
    scanf("%d", &qnt_animal);

    printf("Informe o custo de alimentação (R$/kg): ");
    scanf("%lf", &custo_comida);

    printf("Informe a quantidade de alimentação (kg/animal/dia): ");
    scanf("%lf", &qnt_comida);

    // Calculations
    custo_dia = qnt_animal * custo_comida * qnt_comida;
    qnt_comida_mes = qnt_animal * qnt_comida * 30;
    custo_mes = custo_dia * 30;

    // Output
    printf("\n--- Relatório de Custo ---\n");
    printf("Animal: %s\n", nome_animal);
    printf("Custo estimado p/dia: R$ %.2lf\n", custo_dia);
    printf("Quantidade de comida consumida p/mês (kg): %.2lf\n", qnt_comida_mes);
    printf("Custo estimado p/mês: R$ %.2lf\n", custo_mes);

    return 0;
}