# Fazer um programa que pega N1 e N2 e verifica qual o maior
n1 = int(input("Insira N1"))
n2 = int(input("Insira N2"))

if n1 > n2:
    print(f"{n1} é maior que {n2}")
else:
    print(f"{n2} é maior que {n1}")

#-----------------------------------------------------------------
#Fazer um script que peça um valor e mostre na tela se o valor
#é positivo ou negativo

n1=int(input("Insira N1"))
if n1 < 0:
    print(f"{n1} é negativo")
else:
    print(f"{n1} é positivo")

#-----------------------------------------------------------------
#Fazer um programa que verifique se uma letra digitada é "F" ou "M"
#Conforme a letra, escrever: F - Feminino, M - Masculino, Sexo Invalido

sx = input("Insira seu sexo")
if sx == "M" or sx == "m":
    print("Masculino")
elif sx == "F" or sx == "f":
    print("Feminino")
else:
    print("Sexo Inválido")
#-----------------------------------------------------------------
#Fazer um programa que peça uma nota, entre 0-10, mostre uma mensagem
#caso o valor seja inválido e continue pedindo até que o usuário informe
#um valor válido
while True:
    try:
        n1 = int(input("Insira N1: "))
        if n1 < 0 or n1 > 10:
            print("Entrada inválida. Por favor, insira um número entre 0 e 10.")
        else:
            print("ok")
            break
    except ValueError:
        print("Entrada inválida. Por favor, insira um número inteiro.")
        continue
#-----------------------------------------------------------------
#Faça um programa que leia 5 números e informe o maior numero
# Inicializa a variável para armazenar o maior número
maior_numero = None
contador = 0

print("Digite 5 números:")

while contador < 5:
    try:
        numero = float(input(f"Número {contador + 1}: "))

        if maior_numero is None or numero > maior_numero:
            maior_numero = numero

        contador += 1

    except ValueError:
        print("Entrada inválida. Por favor, digite um número.")

if maior_numero is not None:
    print(f"O maior número digitado foi: {maior_numero}")
else:
    print("Nenhum número válido foi digitado.")
#-----------------------------------------------------------------
#Faça um programa que receba 2 numeros inteiros e gere os numeros inteiros
#que estao no intervalo entre eles
n1 = int(input("Insira N1"))
n2 = int(input("Insira N2"))

for n in range(n1, n2 + 1):
    print(n)
#-----------------------------------------------------------------
#Você recebeu uma lista de salários:
#[1200,3600,750,4500,12000]
#faça um programa que exiba o maior e menor salário
salario = [1200,3600,750,4500,12000]
salario.sort()
print(f"o menor salario é {salario[0]} e o maior salario é {salario[4]}")
#-----------------------------------------------------------------
#Faça um programa que receba uma lista de valores e ao final mostre o maior
#e o menor valor
lst = []

while True:
    el = input("Adicione um número à lista (digite 'fim' para terminar): ")

    if el.lower() == 'fim':
        break

    try:
        numero = float(el)
        lst.append(numero)

    except ValueError:
        print("Por favor, digite um número válido ou 'fim' para terminar.")

if lst:
    print("\nLista final:", lst)
    print(f"O menor número da sua lista é {min(lst)} e o maior é {max(lst)}")
else:
    print("Nenhum número foi adicionado à lista.")



