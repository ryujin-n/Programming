#Manipulacao de strings
# fatiamento
frase="Curso em video Python"
# print(frase[9:14]) //vai de 9 ate 13
# print(frase[9:21:2]) //vai pular de 2 em 2 de 9 ate 21
# print(frase[:5]) //do 0 ate o carácter 5
# print(frase[15:]) //do 15 ate o final
# print(frase[9::3]) // começa do 9, vai ate o final pulando de 3 em 3
##########################################################################
# analise
# len(frase) //determina o tamanho da frase
# print(frase.count('o')) //conta quantas vezes aparece a letra 'o'
# print(frase.count('o',0,13)) //conta quantas vezes aparece a letra 'o' desde 0 ate 13
# print(frase.find("deo")) //determina a localização de dentro do ""
# print(frase.find("Android")) //qnd nn existe, retorna -1
# print('Curso' in frase) //retorna booleano, verifica se existe a palavra dentro da string
##########################################################################
# transformação
# print(frase.replace("Python","Android")) //substitui parametro x por y
# print(frase.upper()) //transforma tudo em maiúsculo
# print(frase.lower()) //transforma tudo em minusculo
# print(frase.capitalize()) //so o primeiro caractere fica em maiúsculo
# print(frase.title()) //diferentemente do capitalize, ele transforma em maiúsculo
# palavras entre espaços
# print(frase.strip()) //remove espaços no começo e final
# print(frase.rstrip()) //remove espaços apenas no final
# print(frase.lstrip()) //remove espaços apenas no começo
##########################################################################
# divisão
# print(frase.split()) //divide em palavras de acordo com os espaços
##########################################################################
# junção
# print('-'.join(frase)) //junta as palavras com caractere dentro do ''
##########################################################################

a=input("Digite um nome: ").strip()
print(f"nome: {a} \nnome maiusculo: {a.upper()} \nnome minusculo: {a.lower()}")
print(f"qtde de letras: {len(a.replace(' ',''))} \nqtde de letras 1o nome: {len(a.split()[0])}")

num=int(input("digite um numero: "))
u= num // 1 % 10
d= num // 10 % 10
c= num // 100 % 10
m= num // 1000 % 10
print(f"unidade: {u} \ndezena: {d}\ncentena: {c}\nmilhar: {m}")


a=input("Digite algo: ")
print("possui a palavra silva?:","SILVA" in a.upper())

a=input("Digite algo: ").strip()
a=a.split()
print("possui santo no começo?:","SANTO" in a[0].upper())

a=input("Digite algo: ").strip()
print(f"""quantas letras a = {a.count('a')}
posição inicial = {a.find('a')+1}
posição final = {a.rfind('a')+1}
""")

a=input("Digite algo: ").strip()
a=a.split()
print(f"""primeiro nome: {a[0]}
ultimo nome: {a[-1]}
""")