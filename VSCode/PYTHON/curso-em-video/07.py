# condições (if)
# sao instruções condicionais
# 1 ###############################################################################
# carro.siga() > carro.esquerda() > carro.siga() > carro.direita() > carro.siga()
# carro.esquerda() > carro.siga() > carro.pare()
##################################################################################
# 2 ##############################################################################
#                 esquerda |>carro.esquerda() > carro.siga() > carro.direita() > carro.esquerda()
#                          |>carro.siga() > carro.direita() > carro.siga()
# carro.siga() > bifurcação <
#                 direita |>carro.direita() > carro.siga() > carro.esquerda() > carro.siga()
#                         |>carro.esquerda() > carro.siga
##################################################
# carro.siga()          |   carro.siga()
# se carro.esquerda()   |   if carro.esquerda():
#   carro.siga()        |       carro.siga()
#   carro.direita()     |       carro.direita()
#   carro.siga()        |       carro.siga()
#   carro.direita()     |       carro.direita()
#   carro.esquerda()    |       carro.esquerda()
#   carro.siga()        |       carro.siga()
#   carro.direita()     |       carro.direita()
#   carro.siga()        |       carro.siga()
# senão                 |   else:
#   carro.direita()     |       carro.direita()
#   carro.siga()        |       carro.siga()
#   carro.esquerda()    |       carro.esquerda()
#   carro.siga()        |       carro.siga()
#   carro.esquerda()    |       carro.esquerda()
#   carro.siga          |       carro.siga
##################################################
# tempo = int(input("Digite a tempo: "))
# if tempo <=3:
#     print("carro novo")
# else:
#     print("carro velho")
# print("==FIM==")
#ou
# print("carro novo"if tempo<=3 else "carro velho")
# print("==FIM==")

# nome = input("Digite seu nome: ")
# if nome == "Miles":
#     print("que nome lindo vey")
# else:
#     print("que nome cis....")
# print(f"bom dia, {nome}")

# n1=float(input("Digite nota1: "))
# n2=float(input("Digite nota2: "))
# media=(n1+n2)/2
#
# if media >= 6:
#     sts="aprovado"
# else:
#     sts="reprovado"
# print(f"media={media:.3f}, voce esta {sts}")
#####################################################
#desafios

import random
from time import sleep
n1=random.randint(0,5)
print("-=-"*20)
print("to pensando num numero...adivinha qual")
print("-=-"*20)
i=int(input("Digite um numero: "))
print("deixa eu ver...")
sleep(2)
if i == n1:
    print("Voce venceu veeyy")
else:
    print("voce perdeu seu porra")

km=float(input("Kms do radar: "))
if km > 80:
    multa=(km-80)*7
    print("multa=R${:.2f}".format(multa))
else:
    print("parabens, voce nao teve multa")

n=int(input("Digite numero: "))
if n % 2 == 0:
    print("Par")
else:
    print("Impar")

km= float(input("quantos kms é a viagem?: "))
if km > 200:
    passagem= km*0.45
else:
    passagem= km*0.50
print("passagem=R${:.2f}".format(passagem))

from datetime import date
ano=int(input("Digite um ano: "))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print("Ano bissexto")
else:
    print("Ano normal")

n1 = float(input("Digite n1: "))
n2 = float(input("Digite n2: "))
n3 = float(input("Digite n3: "))
menor = n1
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
print(f"menor:{menor} \nmaior:{maior}")

s=float(input("Digite seu salario: "))
if s > 1250:
    novo_salario=s+(s*0.10)
else:
    novo_salario=s+(s*0.15)
print("Novo salario=R${:.2f}".format(novo_salario))

l1=float(input("Digite lado1: "))
l2=float(input("Digite lado2: "))
l3=float(input("Digite lado3: "))

if l1 + l2 > l3 and l1 + l3 > l2 and l2+l3 > l1:
    print("Pode ser um triangulo")
else:
    print("nao pode ser um triangulo")
