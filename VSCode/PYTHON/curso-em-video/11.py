#####################################################
# enquanto verdadeiro   |   while True:             #
#   se chao             |       if chao:            #
#      passo            |         passo()           #
#   se buraco           |       if buraco:          #
#       pula            |         pula()            #
#   se moeda            |       if moeda:           #
#       pega            |         pega()            #
#   se trofeu           |       if trofeu:          #
#       pula            |         pula()            #
#       interrompa      |       >>break<<           #
# pega                  |   pega()                  #
#####################################################
# cont = 1
# while cont <= 10:
#     print(cont ,'-> ',end=' ')
#     cont += 1
# print("FIM")
from random import choice, randint

from jedi.inference.helpers import is_number

# n = 0
# cont = 0
# while cont != 999:
#     n = int(input("Digite um numero: "))
#     cont += 1

#     n = 0
# cont = 0
# while cont < 3:
#     n = int(input("Digite um numero: "))
#     cont += 1

# n = s = 0
# while True:
#     n = int(input("Digite um numero: "))
#     if n == 999:
#         break
#     s += n
# print(f"A soma dos numeros: {s}")
#####################################################
#desafios
# n = s = i = 0
# while True:
#     n = float(input("Digite um numero: "))
#     if n == 999:
#         break
#     s += n
#     i += 1
# print(f"A soma dos numeros: {s} \nnumeros digitados: {i}")

# while True: #// enquanto for verdadeiro (loop infinito)
#     n = int(input("\033[0;34;48mInsira um Numero: \033[m")) #// pede numero
#     if n < 0: #// verifica se o numero é negativo
#         print(f"\033[0;31;48mAdeus!\033[m") #// sai do programa
#         break
#     i = 0 #// contador
#     while i < 10: #// enquanto o contador for menor que 10
#         i += 1 #// adiciona 1 no contador
#         print(f"\033[0;33;48m[{n}] x [{i}] = {n * i}\033[m") #// faz a tabuada

# print("-="*10)
# print(f"\033[0;35;48m{"Par ou Impar":>16}\033[m")
# print("-="*10)
# g = 0
# while True:
#     p = input("escolha PAR ou IMPAR [P/I]: ").upper()
#     while p not in "PpIi":
#         print("Digite apenas [P/I]")
#         p = input("escolha PAR ou IMPAR [P/I]: ")
#     p1 = int(input("qual numero vai jogar?: "))
#     lista = ["PAR", "IMPAR"]
#     m = choice(lista)
#     m1 = randint(0,10)
#     s = p1 + m1
#     if s % 2 == 0:
#         res = "PAR"
#     else:
#         res = "IMPAR"
#
#     if (res == "PAR" and p == "P") or (res == "IMPAR" and p == "I"):
#         g =+ 1
#         print("-="*10)
#         print(f"Você ganhou! \nvoce jogou {p1} e o pc jogou {m1} \ntotal de {s} deu {res}!")
#         print("-="*10)
#     else:
#         print("-=" * 10)
#         print(f"Você perdeu! \nvoce jogou {p1} e o pc jogou {m1} \ntotal de {s} deu {res}! \nvoce ganhou {g} vezes consecutivas!")
#         print("-=" * 10)
#         play = input("Quer jogar dnv? [S/N]")
#         if play in "Ss":
#            continue
#         else:
#             break

# mi = h = mm = 0
# while True:
#     i = int(input("Digite idade: "))
#     s = input("Digite seu sexo [M/F]: ").upper()
#     while s not in "MmFf":
#         print("Digite apenas M ou F")
#     if i > 18:
#         mi += 1
#     if s in "Mm":
#         h += 1
#     if s in "Ff" and i < 20:
#         mm += 1
#     p = input("Quer continuar? [S/N]: ").upper()
#     while p not in "SN":
#         print("Digite apenas S ou N")
#         p = input("Quer continuar? [S/N]: ").upper()
#     if p == "N":
#         print(f"""Foram digitados:
#         {mi} maiores de idade
#         {h} homens
#         {mm} mulheres com menos de 20 anos
#         """)
#         break
#     else:
#         continue

# t = l = menor = p2 = mp = 0
# pb = ""
# while True:
#     n = input("Digite nome do produto: ")
#     p = float(input("Digite o preço:R$ "))
#     l += 1
#     t += p
#     if p > 1000:
#         mp += 1
#     if l == 1 or p < menor: #//se for a primeira iteracao, o menor produto vai ser
#         menor = p          #//o primeiro produto, guardando o valor anterior e o
#         pb = n            #// comparando com os proximos, guardando o nome do menor
#     i = ' '
#     while i not in "SN":
#         i = input("Quer continuar? [S/N]: ").strip().upper()[0]
#     if i == "N":
#         print("-="*10)
#         print(f"Compra finalizada com o total de R${t:.2f} \ncom {l} produtos no carrinho \nsendo {pb} o produto mais barato custando R${menor:.2f} \n{mp} produto(s) que custam mais de mil reais")
#         print("-="*10)
#         break

# print("="*30)
# print(f"{"Banco do milhao":^30}")
# print("="*30)
# v = int(input("Digite o valor a ser sacado: "))
# tot = v #//montante = valor total
# cm = 50 #// maior cedula q tem, pq ai vai tirando da maior pra menor
# totc = 0 #// quantidade de cedulas
# while True: #// loop infinito
#     if tot >= cm: #// se o total for maior ou igual a maior cedula
#         tot -= cm #// vai tirando o valor da maior cedula do total
#         totc += 1 #// mostra quantas cedulas serao necessarias
#     else: #// se o valor da maior cedula for maior
#         if totc > 0: #// caso n tenha nenhuma cedula, nn mostra
#             print(f"total de {totc} cedulas de R${cm}")
#         if cm == 50: #// se a maior cedula for 50, agr sera 20
#             cm = 20
#         elif cm == 20: #// se a maior cedula for 20, agr sera 10
#             cm = 10
#         elif cm == 10: #// se a maior cedula for 10, agr sera 1
#             cm = 1
#         totc = 0 #// toda vez q muda o valor da cedula, ela deve ser zerada
#         if tot == 0:
#             break
# print("="*30)

