#variaveis compostas - tuplas()

# lanche = hambúrguer
# lanche = suco
# assim, a atribuição de lanche é substituída de hambúrguer por suco
# lanche = [hambúrguer, suco, pizza, pudim]
# índices->     0         1     2      3

# lanche = ("hamburger","suco","pizza","pudim")
# print(lanche[2]) -> pizza
# print(lanche[0:2]) -> hambúrguer , suco
# print(lanche[1:]) -> suco , pizza, pudim
# print(lanche[-1]) -> pudim
# print(len(lanche)) -> 4

# for c in lanche: ->    hamburger
#    print(c)            suco
#                        pizza
#                        pudim

# As tuplas são IMUTÁVEIS, ou seja, nao da pra modificar, eliminar ou adicionar itens
# -----------------------------------------------------------------------------------
# pratica

# lanche = ("Hambúrguer","Suco","Pizza", "Pudim","Batata frita")
# for c in lanche:
#     print(f"eu vou comer {c}")

# for pos,c in  enumerate(lanche):
#     print(f"eu vou comer {c} na posição {pos}")

# for cont in range(0, len(lanche)):
#     print(f"vou comer {lanche[cont]} na posição {cont}" )

# print("comi pra krl")
# print(sorted(lanche))

# a = (2,5,4)
# b = (5,8,1,2)
# c = b+a # a ordem importa
# # print(a)
# # print(b)
# print(c) #juntou as tuplas
# # print(c.count(5)) // conta quantas vezes aparece o numero especificado
# print(c.index(5,1)) #mostra a posição do numero especificado

# pessoa = ("gustavo", 39, "M", 99.88)
# del pessoa # apaga a tupla inteira
# print(pessoa)
# -----------------------------------------------------------------------------------
# desafios

# num = ("zero","um","dois","tres","quatro",
#        "cinco","seis","sete","oito","nove",
#        "dez","onze","doze","treze","quatorze",
#        "quinze","dezesseis","dezessete","dezoito",
#        "dezenove","vinte")
#
# while True:
#     n = int(input("Digite um numero de 0 a 20: "))
#     if n in range(0,21):
#         break
#     print("Numero invalido")
# print(f"voce digitou o numero {num[n]}")

# t = ("Palmeiras","Flamengo","Cruzeiro Saf","Mirassol",
#      "Bahia","Botafogo","Fluminense","São Paulo",
#      "Atlético Mineiro Saf","Vasco da Gama S.a.f.",
#      "Corinthians","Red Bull Bragantino","Ceará",
#      "Grêmio","Internacional","Vitória","Santos Fc",
#      "Juventude","Fortaleza Ec Saf","Sport Recife",)
#
# print(f"Top 20 do Brasileirão Serie A: {t}")
# print("-=-"*20)
# print(f"5 Primeiros colocados: {t[:5]}")
# print("-=-"*20)
# print(f"4 Ultimos colocados: {t[-4:21]}")
# print("-=-"*20)
# print(f"Times em ordem alfabetica: {sorted(t)}")
# print("-=-"*20)
# print(f"Posição do Corinthians:{t.index("Corinthians")+1} lugar")

# from random import randint
#
# n = (randint(0,10), randint(0,10), randint(0,10), randint(0,10),
#      randint(0,10))
#
# print(f"os numeros gerados foram: ",end="")
# for i in n:
#     print(i,end=' ')
# print(f"\nO maior numero é {max(n)}, o menor numero é {min(n)}")

# t= (int(input("Escreva um numero: ")),
#     int(input("Escreva um numero: ")),
#     int(input("Escreva um numero: ")),
#     int(input("Escreva um numero: ")),)
# e = 0
# p=[]
# print(t)
#
# if t.count(9)==0:
#     print(f"o numero 9 foi mostrado nenhuma vez")
# else:
#     print(f"o numero 9 foi mostrado {t.count(9)} {"vez" if t.count(9) == 1 else "vezes"}")
# if t.count(3):
#     print(f"a posição do primeiro numero 3 foi a {t.index(3)+1}a posicao")
# else:
#     print(f"numero 3 nn foi digitado")
# for i in t:
#     if i % 2 == 0:
#         e = i
#         p.append(e)
# if e == 0:
#     print("Nenhum numero par foi digitado")
# else:
#     print(f"números pares foram: {str(p).replace("[","").replace("]","")}")

# lista= ("Lápis", 1.75, "Borracha", 2, "Caderno", 15.9,
#         "Estojo",25,"Transferidor", 4.2,"Compasso", 9.99,
#         "Mochila",120.32,"Caneta",22.3,"Livro",34.9)
# print("-"*40)
# print(f"{'PAPELARIA DO MILHINHO':^40}")
# print("-"*40)
# for item in range(0,len(lista)):
#     if item % 2 == 0:
#         print(f"{lista[item]:.<30}", end="")
#     else:
#         print(f"R${lista[item]:>7.2f}")
# print("-"*40)

# palavras = ('aprender','programar','linguagem','python',
#             'curso','gratis','praticar','trabalhar',
#             'mercado','programador','futuro')
# for p in palavras:
#     print(f"\nna palavra [{p.upper()}] temos: ", end='')
#     for letra in p:
#         if letra.lower() in 'aeiou':
#             print(letra, end=' ')

