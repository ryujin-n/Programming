qtd = 0
soma = 0
media = 0
valor = float(input("n1"))

while valor > 0:
    soma = soma + valor
    qtd = qtd + 1
    valor = float(input("n1 dnv"))

media = soma / qtd
print("\n soma: ", soma)
print("\n qtd de valores:", qtd)
print("\n media dos valores: ", media)


#----------------------------------------------
#Funcao

def msg1():
    print("Hello World")


def msg2():
    return 'Hello World'


msg1()

texto = msg2()
print(texto)


#----------------------------
def ler_notas():
    n = float(input("n1"))
    return n


def res(n1, n2):
    media2 = (n1 / n2) / 2
    print("media dos valores: ", media2)
    print("n1: ", n1)
    print("n2: ", n2)
    if media2 >= 7:
        print("ok")
    else:
        print("not ok")


a = ler_notas()
b = ler_notas()
res(a, b)
#---------------------------------------------------------
#Manipulacao de coisas :)
#criar arquivo e escreve coisas
arquivo = open("texto.txt", "w")
arquivo.write("Curso python \n")
arquivo.write("aula pratica yey")
arquivo.close()
#--------------------------------
#ler arquivo
leitura = open("texto.txt", "r")
print(leitura.read())
leitura.close()
