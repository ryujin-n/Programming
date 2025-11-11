# nome =input('Digite seu nome: ')
# if nome.upper() == 'MILES':
#     print("que nome bonito vey")
# elif nome.upper() == 'MAKKI' or nome.upper() == 'ANNY':
#     print("que nome homossexual")
# elif nome.upper() == 'AGNES':
#     print("s that my handsome, elegant, intelligent, charming, kind, thoughtful, strong, courageous, creative, brilliant, gentle, humble, generous, passionate, wise, funny, loyal, dependable, graceful, radiant, calm, confident, warm, compassionate, witty, adventurous, respectful, sincere, magnetic, bold, articulate, empathetic, inspiring, honest, patient, powerful, attentive, uplifting, classy, friendly, reliable, ambitious, intuitive, talented, supportive, grounded, determined, charismatic, extraordinary, trustworthy, noble, dignified, perceptive, innovative, refined, considerate, balanced, open-minded, composed, imaginative, mindful, optimistic, virtuous, noble-hearted, well-spoken, quick-witted, deep, philosophical, fearless, affectionate, expressive, emotionally intelligent, resourceful, delightful, fascinating, sharp, selfless, driven, assertive, authentic, vibrant, playful, observant, skillful, generous-spirited, practical, comforting, brave, wise-hearted, enthusiastic, dependable, tactful, enduring, discreet, well-mannered, composed, mature, tasteful, joyful, understanding, genuine, brilliant-minded, encouraging, well-rounded, magnetic, dynamic, radiant-spirited, soulful, radiant-hearted, insightful, creative-souled, justice-minded, reliable-hearted, tender, uplifting-minded, persevering, devoted, angelic, down-to-earth, golden-hearted, gentle-spirited, clever, courageous-hearted, courteous, harmonious, loyal-minded, beautiful-souled, easygoing, sincere-hearted, respectful-minded, comforting-voiced, confident-minded, emotionally strong, respectful-souled, imaginative-hearted, protective, noble-minded, confident-souled, wise-eyed, loving, serene, magnetic-souled, expressive-eyed, brilliant-hearted, inspiring-minded, and absolutely unforgettable, absolutely iconic Agnes Tachyon?")
# else:
#     print("que nome cis....")
# print(f"tenha un good dia {nome}")
#################################################################################################
#desafios
from datetime import date

# c=float(input('qual o valor da casa?:R$ '))
# s=float(input('qual o seu salario?:R$ '))
# a=float(input('em quantos anos?: '))
# ps= c / (a*12)
# mm = s*30/100
# if ps <= mm:
#     print(f"prestacao=R${ps:.2f}, voce pode comprar!")
# else:
#     print(f"prestacao = R${ps:.2f}, seu salario nao condiz, negado")

# print("=-=-="*10)
# print(f"{'Calculadora foda':>33}")
# print("=-=-="*10)
# num=int(input("Digite um numero: "))
# i=int(input("""Converter para:
# [ 1 ] - binario
# [ 2 ] - octal
# [ 3 ] - hexadecimal
# digite sua escolha: """))
# if i==1:
#     binario=bin(num)
#     print(f"binario de {num}: {binario[2:]}")
# elif i==2:
#     octal=oct(num)
#     print(f"octal de {num}: {octal[2:]}")
# elif i==3:
#     hexadecimal=hex(num)
#     print(f"hexadecimal de {num}: {hexadecimal[2:]}")
# else:
#     print("Digite uma escolha valida")

# n1 = float(input("Digite n1: "))
# n2 = float(input("Digite n2: "))
#
# if n1 > n2:
#     print(f"{n1} é maior que {n2}")
# elif n2 > n1:
#     print(f"{n2} é maior que {n1}")
# else:
#     print("Ambos sao iguais")

# from datetime import date
# i=int(input("digite ano de nascimento: "))
# f=2017 - i
# if f < 18:
#     print(f"voce tem {f} anos,vai precisar se alistar daqui a {18-f} anos \nvolte em {2017+(18-f)}")
# elif f == 18:
#     print(f"voce tem {f} anos, precisa se alistar agora")
# else:
#     print(f"voce tem {f} anos, ja passou da hora filho, voce ta {f-18} anos atrasado \nseu alistamento deveria ter sido em {2017-(f-18)}")

# n1=float(input("Digite nota1: "))
# n2=float(input("Digite nota2: "))
# media=(n1+n2)/2
#
# if media < 5:
#     print("burro do kct")
# elif media >= 7:
#     print("parabens")
# else:
#     print("burrinho mas recuperável")

# f=int(input("digite a idade: "))
# i=2017 - f
# if i <= 9:
#     print(f"idade:{i} \ncategoria: MIRIM")
# elif i <= 14:
#     print(f"idade:{i} \ncategoria: INFANTIL")
# elif i <= 19:
#     print(f"idade:{i} \ncategoria: JUNIOR")
# elif i <= 25:
#     print(f"idade:{i} \ncategoria: SENIOR")
# else:
#     print(f"idade:{i} \ncategoria: MASTER")

# l1=float(input("Digite lado1: "))
# l2=float(input("Digite lado2: "))
# l3=float(input("Digite lado3: "))
#
# if l1 + l2 > l3 and l1 + l3 > l2 and l2+l3 > l1:
#     if l1 == l2 and l1 == l3:
#         print("Pode ser um triangulo e ele é equilátero")
#     elif l1 == l2 or l1 == l3 or l2 == l3:
#         print("Pode ser um triangulo e ele é isosceles")
#     elif l1 != l2 or l1 != l3 or l2 != l1:
#         print("Pode ser um triangulo e ele é escaleno")
# else:
#     print("nao pode ser um triangulo")

# print("=-=-="*10)
# print(f"{'Calculadora IMC foda':>31}")
# print("=-=-="*10)
# p=float(input("Digite seu peso (kg): "))
# a=float(input("Digite sua altura (m): "))
# imc=p/a**2
# if imc < 18.5:
#     print(f"imc={imc:.1f} (Abaixo do peso)")
# elif 18.5 <= imc < 25:
#     print(f"imc={imc:.1f} (Peso ideal)")
# elif 25 <= imc < 30:
#     print(f"imc={imc:.1f} (Sobrepeso)")
# elif 30 <= imc < 40:
#     print(f"imc={imc:.1f} (Obesidade)")
# else:
#     print(f"imc={imc:.1f} (Obesidade morbida)")

# p=float(input("Digite preço:R$ "))
# pg=int(input("""[ 1 ] - pix
# [ 2 ] - à vista no cartão
# [ 3 ] - 2x no cartão
# [ 4 ] - 3x ou mais no cartão
# Digite forma de pagamento: """))
#
# px=p-(p*0.1)
# c1=p-(p*0.05)
# c2=p + (p * 0.2)
#
# if pg==1:
#     print(f"seu carrinho deu: R${px:.2f}")
# elif pg==2:
#     print(f"seu carrinho deu: R${c1:.2f}")
# elif pg==3:
#     print(f"seu carrinho deu: R${p:.2f}")
# elif pg==4:
#     parcela=int(input("Digite parcela: "))
#     print(f"seu carrinho deu: R${c2:.2f} \ncom {parcela} parcela(s) de {c2/parcela:.2f}")
# else:
#     print("opção invalida")

# from time import sleep
# from random import randint
# print("=-=-="*10)
# print(f"{'Jokenpô foda':>31}")
# print("=-=-="*10)
# print("Vamos jogar um jogo :3?")
# sleep(1)
# i=int(input("""1 - Pedra
# 2 - Papel
# 3 - Tesoura
# escolha: """))
# print("JO")
# sleep(1)
# print("KEN")
# sleep(1)
# print("PO!!!")
#
# e=randint(1,3)
# if i==e:
#     print("=-="*10)
#     print("empate :(")
#     print("=-="*10)
#
# elif i==1 and e==2 or i==2 and e==3 or i==3 and e==1:
#     print("=-="*10)
#     print("ganhei veyyy!!")
#     print("=-="*10)
# else:
#     print("=-="*10)
#     print("voce ganhou...")
#     print("=-="*10)
