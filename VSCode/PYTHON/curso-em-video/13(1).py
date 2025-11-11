# Variáveis Compostas - Listas[]
# lanche = (hambúrguer, suco, pizza, pudim)
# índices->     0         1     2      3

# lanche = ("hamburger","suco","pizza","pudim")
# lanche[3] = "picolé"
# print(lanche) -> hamburger, suco, pizza, picolé

# ao contrário das tuplas, as listas sao mutáveis, ou seja
# é possível modificar, adicionar, remover itens dentro da lista

# adicionar itens
# lanche.append('cookie')
# print(lanche) -> hamburger, suco, pizza, picolé, cookie //inseriu o cookie no final da lista
# lanche.insert(0,hotdog)
# print(lanche) -> hotdog, hamburger, suco, pizza, picolé, cookie //inseriu hotdog na posição 0
# e renumerou as outras

# deletar itens
# del lanche[3] // deleta o item e o índice, reposicionando o resto da lista
# print(lanche) -> hotdog, hamburger, suco, picolé, cookie
# índices->           0       1        2      3       4
# lanche.pop() //elimina o ultimo elemento, mas pode ser usado com referencia
# print(lanche) -> hotdog, hamburger, suco, pizza, picolé
# if "pizza" in lanche:
#     lanche.remove("pizza")
# print(lanche) -> hotdog, hamburger, suco, picolé, cookie

# valores = list(range(4,11)) //ja cria a estrutura com os elementos já em ordem
# print(valores) -> 4, 5, 6, 7, 8 , 9, 10

# valores = [8,2,5,4,9,3,0]
# valores.sort() //ordena em ordem crescente
# print(valores) -> 0, 2, 3, 4, 5, 8, 9
# valores.sort(reverse=True) //ordena em ordem decrescente
# print(valores) -> 9, 8, 5, 4, 3, 2, 0
# len(valores) -> 7 //conta a quantidade de elementos dentro da lista
# -----------------------------------------------------------------------
# pratica

# n = (2,5,9,1)
# n[2] = 3 //da erro
# n = [2,5,9,1]
# n[2] = 3
# # n[4] = 7 // erro pq n existe índice 4
# n.append(7)
# n.sort(reverse=True)
# n.insert(2,2)
# # n.pop(2)
# if 4 in n:
#     n.remove(4)
# else:
#     print("nao tem numero 4")
# print(n)
# print(f"essa lista tem {len(n)} elementos")

# valores = []
# for cont in range(0, 5):
#     valores.append(int(input("Digite um valor: ")))
# for c,v in enumerate(valores):
#     print(f"na posição {c}, tem o valor {v}")
# print("Fim")

# a = [2,3,4,7]
# # b = a
# # b[2] = 8
# # print(f"lista A: {a}")
# # print(f"lista B: {b}") # ambas serão iguais, pois tem uma ligação
# b = a[:]
# b[2] = 8
# print(f"lista A: {a}")
# print(f"lista B: {b}") # agora B é uma copia de A
# -----------------------------------------------------------------------

from random import randint

# num = []
# for n in range(0,5):
#     num.append(int(input(f"Digite um valor p/ posição {n}: ")))
# mx = max(num)
# mn = min(num)
# maior_num = []
# menor_num = []
# print("-"*20)
# print(f"Lista digitada: {num}")
# for pos,cont in enumerate(num):
#     if cont == mx:
#         maior_num.append(pos)
#     if cont == mn:
#         menor_num.append(pos)
# print(f"Maior numero: [{mx}] na posição: {str(maior_num).replace("[", "").replace("]","")}")
# print(f"Menor numero: [{mn}] na posição: {str(menor_num).replace("[", "").replace("]","")}")

# lst = []
# while True:
#     num = int(input("Digite um valor: "))
#     if num in lst:
#         print("Número duplicado!")
#     else:
#         lst.append(num)
#     while True:
#         q = input("Quer continuar? [S/N]: ")
#         if q in 'Nn':
#             lst.sort()
#             print("-"*50)
#             print(f"você digitou os valores: {lst}")
#             break
#         elif q in 'Ss':
#             break
#         else:
#             print("Digite uma opção válida!")
#     if q in 'Nn':
#         break

# lst = []
# for i in range(0, 5):
#     num = int(input("Digite um valor: "))
#     pos = 0
#     while pos < len(lst) and lst[pos] < num:
#         pos += 1
#     print(f"{num} foi colocado na posição {"final" if i == 0 or num > lst[-1] else pos}")
#     lst.insert(pos, num)
# print(f"Valores digitados: {lst}")

# lst = []
# i = 0
# n5 = 0
# inx = []
# while True:
#     num = int(input("Digite um valor: "))
#     lst.append(num)
#     i += 1
#     if num == 5:
#         inx.append(i)
#         n5 += 1
#     while True:
#         p = input("Deseja continuar? [S/N]: ")
#         if p not in "SsNn":
#             print("Digite apenas S ou N")
#         else:
#             break
#     if p in "Nn":
#         lst.sort(reverse=True)
#         print("-"*50)
#         print(f"Números digitados: {lst}")
#         print(f"Quantidade de números da lista: {len(lst)}")
#
#         if n5 != 0:
#             print(f"Número 5 foi digitado {n5} {"vez" if n5 == 1 else "vezes"} e está na(s) posição(ões): {inx}")
#         else:
#             print("Número 5 não foi digitado")
#         print("-" * 50)
#         break

# lst = []
# even = []
# odd = []
# while True:
#     num = int(input("Digite um valor: "))
#     lst.append(num)
#     if num % 2 == 0:
#         even.append(num)
#     else:
#         odd.append(num)
#     while True:
#         q = input("Quer continuar? [S/N]: ")
#         if q not in "NnSs":
#             print("Digite apenas S ou N")
#         else:
#             break
#     if q in "Nn":
#         print("-" * 50)
#         print(f"Números digitados: {lst}")
#         print(f"Números Pares: {even}")
#         print(f"Números Ímpares: {odd}")
#         print("-" * 50)
#         break

