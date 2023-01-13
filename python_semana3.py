#Dados 3 numeros saber quantos estão acima da media
X = float(input())
Y = float(input())
Z = float(input())

media = (X + Y + Z) // 3

if media < X and media < Y:
  print(2)
elif media < Z and media < Y:
 print(2)
elif media < Z and media < X:
 print(2)
elif media < X or media < Y or media < Z:
  print(1)
elif media == X and media == Y and media == Z:
 print(0)

else:
  print(3)

#Dados 3 numeros saber o menor deles
num1 = int(input())
num2 = int(input())
num3 = int(input())

menor = num1
if menor >num2:
  menor = num2  
if menor >num3:
  menor = num3
  
print(menor)