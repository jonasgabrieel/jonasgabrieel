#Intervalo
valor = float(input())

if valor>=0 and valor<=25:
  print('Intervalo [0,25]')
elif valor>25 and valor<=50:
  print('Intervalo (25,50]')
elif valor>50 and valor<=75:
  print('Intervalo (50,75]')
elif valor>75 and valor<=100:
  print('Intervalo (75,100]')
else:
  print('Fora de intervalo')


  #Intermediario de 3 numeros
n1 = int(input())
n2 = int(input())
n3 = int(input())

if n1 > n2 and n2 > n3 or n3 > n2 and n2 > n1:
  print(n2)
if n1 > n3 and n3 > n2 or n2 > n3 and n3 > n1:
  print(n3)
if n2 > n1 and n1 > n3 or n3 > n1 and n1 > n2:
  print(n1)

  
 #Conta de agua
consumo = int(input())
soma = 7

while consumo > 0 :
  if consumo > 100:
    soma = soma + 5
  elif consumo > 30 and consumo <= 100:
    soma = soma + 2
  elif consumo > 10 and consumo <= 30: 
    soma = soma +1 
  consumo = consumo -1
print(soma)

#Comparacao de cotacao de gasolina
gasoUS = float(input())
gasolinaBR = float(input())
cotacao = float(input())
gasolinaUS = gasoUS/3.80*cotacao

if gasolinaUS == gasolinaBR:
    print('Gasolina EUA: R$','%.2f' %gasolinaUS)
    print('Gasolina Brasil: R$','%.2f' %gasolinaBR)
    print('Igual')
else:
    if gasolinaUS < gasolinaBR:
         print('Gasolina EUA: R$','%.2f' %gasolinaUS)
         print('Gasolina Brasil: R$','%.2f' %gasolinaBR)
         print('Mais barata nos EUA')
    elif gasolinaUS > gasolinaBR:
        print('Gasolina EUA: R$','%.2f'%gasolinaUS)
        print('Gasolina Brasil: R$','%.2f' %gasolinaBR)
        print('Mais barata no Brasil')

#Imposto de renda
salario = float(input())
imposto = 0 

if salario <= 2000:
  print('Isento')

elif salario <= 3000:
  imposto = (salario-2000)*0.08
  print('R$', '%.2f' %imposto)

elif salario <= 4500:
  imposto = (salario -3000)*0.18 + 80
  print('R$','%.2f' %imposto)
else:
  imposto = (salario-4500)*0.28 +350 
  print('R$','%.2f' %imposto)


#Conta de multiplos
num1 = int(input())
num2 = int(input())
N = 1
soma = 0

while N > 0 and N < 50:
  if N % num1 == 0 and N % num2 == 0:
    soma = soma + 1
  N = N + 1

print(soma)
  
#RPG
forca = int(input())
inteli= int(input())
destre= int(input())
furtiv= int(input())
peso  = int(input())

if forca > 5 and destre > 5 and peso >5:
  profissao = "Knight"
elif forca < 5 and inteli > 5 and furtiv > 5 and peso <5:
  profissao = "Mage"
elif forca > 5 and inteli >5 and destre >5 and furtiv > 5:
  profissao = "Paladin"
else:
  profissao = "Orc"
  
print(profissao)

#Clasificação de triangulos
def tipo_triangulo(lado1,lado2,lado3):
    if (lado1+lado2<=lado3) or (lado1+lado3<=lado2) or(lado2+lado3<=lado1):
        return "INVALIDO"
    elif lado1==lado2==lado3:
        return "EQUILATERO"
    elif (lado1==lado2) or (lado2==lado3) or (lado1==lado3):
        return "ISOSCELES"
    else:
        return "ESCALENO"

while True:
    lista=input().split()
    item1=lista[0]
    if item1=="FIM":
        break
    lado1=int(lista[0])
    lado2=int(lista[1])
    lado3=int(lista[2])
    triangulo=tipo_triangulo(lado1,lado2,lado3)
    print(triangulo)