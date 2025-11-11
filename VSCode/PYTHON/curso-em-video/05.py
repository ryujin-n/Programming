from math import floor
n=float(input("Digite um numero: "))
print(f"a parte inteira de {n} é: {floor(n)}")

from math import hypot
c1=float(input("Digite o primeiro cateto: "))
c2=float(input("Digite o segundo cateto: "))

h=hypot(c1,c2)
print(f"hipotenusa ={h:.2f}")
# h= sqrt(pow(c1,2)+pow(c2,2))

from math import cos, sin, tan, radians

ang=float(input("Digite um grau: "))
sen=sin(radians(ang))
cos=cos(radians(ang))
tan=tan(radians(ang))
print(f"sen= {sen:.2f} \ncos= {cos:.2f} \ntan= {tan:.2f}")

from random import choice
n1=input("Digite aluno1: ")
n2=input("Digite aluno2: ")
n3=input("Digite aluno3: ")
n4=input("Digite aluno4: ")
lista=[n1,n2,n3,n4]
escolhido=choice(lista)
print(escolhido)

from random import shuffle
n1=input("Digite aluno1: ")
n2=input("Digite aluno2: ")
n3=input("Digite aluno3: ")
n4=input("Digite aluno4: ")
lista=[n1,n2,n3,n4]
shuffle(lista)
print(lista)

import pygame
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('ex.mp3')
pygame.mixer.music.play()
pygame.event.wait()