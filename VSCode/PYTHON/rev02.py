#Jogo de Adivinhação
import random
i = 0
venceu = False
rand = random.randint(1,100)
while not venceu:
   n1 = int(input("Insira N1: "))
   i+=1
   if n1 < rand:
    print("o numero segredos é um poquinho maior")
   elif n1 > rand:
    print("o numero segredos é um poquinho menor")
   elif n1 == rand:
    venceu = True
    print("Voce venceu!!!")
    print(f"tentativas: {i} ")