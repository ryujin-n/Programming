#####################################################
# laco c no intervalo(1,10) | for c in range(1,10): #
#   passo                   |     passo()           #
# pega                      | pega()                #
#####################################################
# laco c no intervalo(0,3)  | for c in range(0,3)   #
#   passo                   |   passo               #
#   pulo                    |   pulo                #
# passo                     | passo                 #
# pega                      | pega                  #
#####################################################
# laco c no intervalo(0,3)  | for c in range(0,3)   #
#   se moeda                |   if moeda            #
#      pega                 |      pega             #
#   passo                   |   passo               #
#   pulo                    |   pulo                #
# passo                     | passo                 #
# pega                      | pega                  #
#####################################################

# for c in range(0,7,2):
#     print(c)
# print("fim")

# for c in range(0,7,-1):
#     print(c)
# print("fim")

# n=int(input("digite um numero: "))
# f=int(input("digite outro numero: "))
# p=int(input("digite outro numero: "))
# for c in range(n,f+1,p):
#     print(c)
# print("fim")

# for c in range(0,3):
#     n=int(input("Digite um numero: "))
# print("fim")

# s=0
# for c in range(0,4):
#     n=int(input("Digite um numero: "))
#     s += n
# print(f"somatoria= {s}")
################################################
# desafios
#
from time import sleep
for c in range(10,0,-1):
    print(f"\033[0;35;48m{c}\033[m")
    sleep(1)
print("\033[0;31;48mFELIZ 2012!!\033[m")

for c in range(2,51,2):
    print(c)
print("fim")

i = 0
s = 0
for c in range(1,501,2):
    print(c)
    if c % 3 == 0:
        s += 1
        i += c
print(f"soma dos impares multiplos de 3 de {s} valores é = {i}")

i=1
n=int(input("Digite um numero: "))
print("=-="*6)
for c in range(0,10):
    m= n * i
    print(f"| [ {n} x {i} ] = {m}"," |")
    i += 1
print("=-="*6)


p=0
for c in range(0,6):
    n=int(input("digite um numero: "))
    if n%2 == 0:
        p += n
print(f"somatoria dos pares = {p}")

p=int(input("Insira o primeiro elemento: "))
r=int(input("Insira a razão: "))
d = p + (10-1) * r #//d= primeiro numero + (10-1) * razão
for i in range(p,d + r,r):
    print(i)


num = int(input("Digite um numero: "))
tot = 0
for i in range(1,num+1):
    if num % i == 0:
        print("\033[33m", end="")
        tot += 1
    else:
        print("\033[31m",end="")
    print(f"{i} ",end="")
print(f"\033[m\nO numero {num} foi divisivel {tot} vez(es)")
if tot == 2:
    print("\033[32mEle é PRIMO!", end="")
else:
    print("\033[31mEle NAO é primo!", end="")

p = input("Digite uma frase: ").strip().upper()
p1 = p.split()
j = ''.join(p1)
i = j[::-1]
""" for letra in range(len(j)-1,-1,-1):
     i += j[letra] """
if i==j:
    print(f"\033[32m{p} ao contrario é {i}, logo é um palindromo")
else:
    print(f"\033[31m{p} ao contrario é {i}, logo NAO é um palindromo")

l=2017
maior = 0
menor = 0
for i in range(0,7):
    n=int(input("digite ano de nascimento: "))
    m=2017-n
    if m >= 21:
        maior += 1
    else:
        menor += 1
print(f"maiores de idade: {maior} \nmenores de idade: {menor}")

#//peso = []
menor = 0
maior = 0
for x in range (1,6):
    p=float(input("Digite um peso: "))
    if x == 1: # // verifica se é a primeira iteração
        maior = p # //maior e menor eram 0, se é a primeira iteração, então o primeiro numero vai ser tanto o menor quanto o menor
        menor = p
    else:
        if p > maior: # //se ja não é mais a primeira iteração, agora começa a comparar os números com o anterior
            maior = p
        if p < menor:
            menor = p

    # //peso.append(p)
    # //peso.sort()
# //print(f"menor peso: {peso[0]} \nmaior peso: {peso[-1]}")
print(f"maior peso: {maior}kg \nmenor peso: {menor}kg")

mulheres=0
soma=0
mh=0
nv=""
for i in range(0,4):
    print("=-="*10)
    nome=input('Digite seu nome: ')
    idade=int(input('Digite sua idade: '))
    sexo=input('Digite seu sexo (M/F): ').strip()
    soma += idade
    if i == 0 and sexo in 'Mm':
        mh = idade
        nv = nome
    if sexo in 'Mm' and idade > mh:
        mh=idade
        nv = nome
    if sexo in 'Ff' and idade>20:
        mulheres+=1
media = soma/4
print(f"a média do grupo é: {media:.2f} \nExistem {mulheres} mulher(es) com menos de 20 anos \no homem mais velho se chama {nv.capitalize()} e tem {mh} anos")

