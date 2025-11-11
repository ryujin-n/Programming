#####################################################
# enquanto nao maça     |   while not maça:         #
#   passo               |       passo()             #
# pega                  |   pega()                  #
#####################################################
# enquanto nao maça     |   while not maça:         #
#   se chao             |       if chao:            #
#      passo            |         passo()           #
#   se buraco           |       if buraco:          #
#       pula            |         pula()            #
#   se moeda            |       if moeda:           #
#       pega            |         pega():           #
# pega                  |   pega()                  #
#####################################################
# for c in range(1,10):
#     print(c)
# print("fim")
from math import factorial
from time import sleep

# c = 1
# while c < 10:
#     print(f"\033[0;36;48m{c}\033[m")
#     c += 1
# print(f"\033[0;31;48mfim\033[m")

# for c in range(1,5):
#     n = int(input("digite um numero: "))
# print(f"\033[0;35;48mfim\033[m")

# n=1
# while n != 0:
#     n = int(input("digite um numero: "))
# print(f"\033[0;35;48mfim\033[m")

# r = "S"
# while r in "Ss":
#     n = int(input("digite um numero: "))
#     r = str(input("continuar? [S/N]: "))
# print(f"\033[0;35;48mfim\033[m")

# n = 1
# p = 0
# i = 0
# while n != 0:
#     n = int(input("digite um valor: "))
#     if n != 0:
#         if n % 2 == 0:
#             p += 1
#
#         else:
#             i += 1
# print(f"pares = {p} \nimpares = {i}")
#####################################################
#desafios

# sexo = input("Digite seu sexo (M/F): ")
# while sexo not in 'MmFf':
#     print("digite corretamente")
#     sexo = input("Digite seu sexo (M/F): ")

# from random import randint
# from time import sleep
# print("=-="*10)
# print(f"\033[0;35;48m{"Jogo da Adivinhação":>24}\033[m")
# print("=-="*10)
# print("Vamos jogar um jogo?")
# sleep(1)
# i = randint(0,10)
# t=0
# acertou = False
#
# while not acertou:
#     n = int(input("digite um numero: "))
#     if i==n:
#         acertou = True
#     else:
#         if i<n:
#             print("menos...")
#         if i > n :
#             print("mais...")
#         t += 1
# print(f"Voce venceu! \ntentativas = {t}")

# n1 = int(input("Digite um número: "))
# n2 = int(input("Digite um número: "))
# menu=0
# while menu != 5:
#     menu = int(input("""    [ 1 ] - Somar
#     [ 2 ] - Multiplicar
#     [ 3 ] - Maior
#     [ 4 ] - Novos números
#     [ 5 ] - Sair
# >>>>> """))
#     if menu == 1:
#         soma = n1 + n2
#         print(f"A soma de {n1} + {n2} = {soma} ")
#         print("=-="*10)
#     elif menu == 2:
#         prod = n1 * n2
#         print(f"O resultado de {n1} x {n2} = {prod} ")
#     elif menu == 3:
#         if n1 > n2:
#             maior = n1
#         else:
#             maior = n2
#         print(f"Entre {n1} e {n2}, {maior} é o maior ")
#     elif menu == 4:
#         print("Informe novos valores")
#         n1 = int(input("Digite um número: "))
#         n2 = int(input("Digite um número: "))
#     elif menu == 5:
#         print("Saindo...")
#         sleep(2)
#         print("bye bye")
#         exit()
#     else:
#         print("=-="*10)
#         print("Digite uma opção válida")
#         print("=-="*10)

# n = int(input("Digite um numero: "))
# sleep(1)
# print(f"Calculando {n}!...")
# c = n
# f = 1
# for i in range(n,0,-1):
#     print(i, end="")
#     print(" x " if i > 1 else " = ", end="")
#     f *= c
#     c -= 1
# print(f"{f}")

# n = int(input("Digite um numero: "))
# sleep(1)
# print(f"Calculando {n}!...")
# c = n
# f = 1
# while c > 0:
#     print(c, end="")
#     print(" x " if c > 1 else " = ", end="")
#     f *= c
#     c -= 1
# print(f"{f}")

# n1 = int(input("Insira primeiro termo: "))
# r = int(input("Insira razão: "))
# t = n1
# cont = 1
#
# while cont <= 10:
#     print("{}".format(t), end="")
#     print(" -> " if cont != 10 else " | Fim", end="")
#     t += r
#     cont += 1

# n1 = int(input("Insira primeiro termo: "))
# r = int(input("Insira razao: "))
# t = n1
# cont = 1
# tot = 0
# p = 10
# while p !=0:
#     tot = tot + p
#     while cont <= tot:
#         print(f"{t}",end="")
#         print(" -> " if cont != 10 else " | pausa ", end="")
#         t += r
#         cont +=1
#     p = int(input("mais termos? (0 = nao): "))
# print(f"Fim \n{tot} termos mostrados")

# n1 = int(input("Insira um termo: "))
# t1 = 0
# t2 = 1
# print("~"*30)
# print(f"{t1} -> {t2}",end="")
# cont = 3
# while cont <= n1:
#     t3 = t1 + t2
#     print(f" -> {t3}",end="")
#     t1 = t2
#     t2 = t3
#     cont += 1
# print(" -> FIM")
# print("~"*30)

# num = cont = soma = 0
# num = int(input("Insira um numero [999 pra parar]: "))
# while num != 999:
#     soma += num
#     cont += 1
#     num = int(input("Insira um numero [999 pra parar]: "))
# print(f"fim \nnumeros digitados = {cont} \nsoma = {soma}")

# num = int(input("Insira um numero: "))
# q = input("Quer continuar? [S/N] ")
# cont = 1
# soma = num
# while q not in "SsNn":
#         print("Digite apenas S ou N")
#         q = input("Quer continuar? [S/N] ")
# while q in 'Ss':
#         num2 = int(input("Insira um numero: "))
#         soma += num2
#         if num < num2:
#             maior = num2
#             menor = num
#         else:
#             maior = num
#             menor = num2
#         q = input("Quer continuar? [S/N] ")
#         cont += 1
# media = soma / cont
# print(f"voce digitou {cont} valores \nmaior = {maior} \nmenor = {menor} \nmedia = {media:.2f}")
