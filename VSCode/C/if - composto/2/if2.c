#include <stdio.h>  
#include <stdlib.h>
#include <locale.h>

int main()
{

    double salario, salario_bruto_ajustado, aumento, salario_liquido; //declaracao de variaveis
    const char *porcentagem_aumento; 

    setlocale(LC_ALL, "pt_BR.UTF-8"); //pra ter acento e ç
    
    printf("Insira o salário bruto atual: R$ "); //pergunta o salario pro usuario
    scanf("%lf", &salario); //coloca o valor q o usuario forneceu do tipo double (%lf) dentro da variavel salario

    if (salario <= 3000.0) //condicional 1 , se o valor for menor ou igual a 3000, ele vai aplicar 15,45% de aumento
    {
        aumento = salario * 0.1545;
        porcentagem_aumento = "15,45%";
    }
    else if (salario <= 5500.0)  //condicional 2 , se o valor for menor ou igual a 5500, ele vai aplicar 10,15% de aumento
    {
        aumento = salario * 0.1015;
        porcentagem_aumento = "10,15%";
    }
    else //se nenhuma das condicionais forem verdadeiras, ele vai aplicar 7,5% de aumento
    {
        aumento = salario * 0.075;
        porcentagem_aumento = "7,5%";
    }

    salario_bruto_ajustado = salario + aumento; //aqui a gente calcula pra tirar os impostos da mesma forma q a gente fez pra calcular o aumento, soq dessa vez, a gente ta tirando dinheiro
    salario_liquido = salario_bruto_ajustado * 0.795;  

    printf("\n=============== RESUMO ===============\n");
    printf("Salário original:    R$ %10.2f\n", salario);
    printf("Aumento (%s):      R$ %10.2f\n", porcentagem_aumento, aumento);
    printf("Salário bruto:       R$ %10.2f\n", salario_bruto_ajustado);
    printf("Impostos (20.5%%):   R$ %10.2f\n", salario_bruto_ajustado * 0.205);
    printf("--------------------------------------\n");
    printf("Salário líquido:     R$ %10.2f\n", salario_liquido);
    printf("======================================\n");

    return 0;
}