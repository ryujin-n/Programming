# #Operadores aritmeticos
# # + adicao
# a=5+2
# print(a)
# # - subtracao
# a= 5-2
# print(a)
# # * multiplicacao
# a=5*2
# print(a)
# # / divisao
# a=5/2
# print(a)
# # ** potencia
# a= 5**2
# print(a)
# # // divisao inteira
# a= 5//2
# print(a)
# # % modulo (resto da divisao)
# a= 5%2
# print(a)

# #Ordem de precedencia
# # 1- ()
# # 2- **
# # 3- *, /, //, %
# # 4- *, -

################################
#desafios
n=int(input("Digite um numero: "))
# print("n={} \nantecessor={} \nsucessor={} \n".format(n,(n-1),(n+1)))
print("dobro={} \ntriplo={} \nraiz quadrada={:.3}".format(n*2,(n*3),pow(n,(1/2))))

n1=float(input("Digite nota1: "))
n2=float(input("Digite nota2: "))

media=(n1+n2)/2
print("media={:.3}".format(media))

m=float(input("Digite em metros: "))
km=m*0.0001
hm=m*0.001
dam=m*0.1
dm=m*10
cm=m*100
mm=m*1000
print("\nkm={}km \nhm={}hm \ndam={}dam \nm={}m \ndm={}dm \ncm={}cm \nmm={}mm".format(km,hm,dam,m,dm,cm,mm))

n=int(input("digite um numero: "))
i = 0
print("-" * 15)
while i<=10:
    print(f"{n} x {i} = {n*i}")
    i = i + 1
t=11
for i in range(t):
    print(f"{n} x {i} = {n * i}")
    i = i + 1
print("-"*15)

r=float(input("digite um valorem reais:R$ "))
print("voce pode comprar U${:.4} !".format(r/3.27))

l=float(input("Digite a largura: "))
t=float(input("Digite a altura: "))
area= l*t
tinta=area/2
print("area={:.2f}m²\nvoce vai precisar de {:.3} litros de tinta".format(area,tinta))

i=float(input("insira um preço:R$ "))
print("preço com 5% de desconto fica R${:.2f}".format(i-(i*0.05)))

s=float(input("Digite um salario: "))
print("salario com 15% de aumento sera: R$ {:.2f}".format(s+(s*0.15)))

c=float(input(f"Digite uma temperatura em Celsius:"))
f=(c*9/5)+32
print("celsius:{}C° \nfahrenheit:{}F°".format(c,f))

d=int(input("quantos dias vc alugou?: "))
km=float(input("quantos km vc percorreu?: "))
total=(km * 0.15)+(d * 60)
print(f"seu total é: R${total:.2f}")