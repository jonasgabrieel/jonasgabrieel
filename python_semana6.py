#Soma de multiplos
n = int(input())
soma = 0
x = 1

while x < n:
  if x%3 == 0 or x%5 ==0:
    soma = soma + x
  x    = x + 1
print(soma)

#Somando multiplos num intervalo
n1 = int(input())
n2 = int(input())
menor = n1
maior = n2

if n1 > n2:
  temp = n1
  n1    = n2
  n2 = temp

comeco = n1
soma = 0
while comeco <= n2:
  if comeco > 0:
    soma = soma + comeco
  comeco = comeco +1

print(soma)

#Loop de impares
entrada1 = int(input())
entrada2 = int(input())

while (entrada1 <= entrada2):
 if entrada1 % 2 != 0:
   print(entrada1)
 entrada1 = entrada1 + 1

 #Capacidade do elevador
 a, b = input().split()
leitura = int(a)
capacidade = int(b)

valor = ''
soma = 0
while leitura > 0:
     c, d = input().split()
     sairam = int(c)
     entraram = int(d)
     soma = soma + (entraram - sairam)
     if soma > capacidade:
        valor = 'S'
        break
     valor = 'N'
     leitura = leitura - 1
  
print(valor)

#Calculando uma serie
N = int(input())

i = 0
soma = 0
e = 0
valor = ""
while N > 0:
   soma = soma + ((1+i)/(3+e))
   e = e + 3
   i = i + 1
   if N == 1:
      valor = valor + str(i) + '/' + str(e)
   else:
      valor = valor + str(i) + '/' + str(e) + ' + '
   N = N - 1
   
print(valor)
print('%.2f' % soma)

#Economia e meta
i = 0
soma = 0
valoranterior = 0
a = 0
while i < 7:
   valor = float(input())
   if (valor - valoranterior >= 0.5):
      a = a + 1
   soma = soma + valor
   valoranterior = valor
   i = i + 1
   
print("R$",'%.2f' % soma)
print(a-1)

#Eleiçãoes em petropoles
total = 0
vencedor = 0
x = 0
y = 0
z = 0
w = 0
while True:
   voto = int(input())
   if voto == 83:
      x = x + 1
      total = total + 1
   elif voto == 93:
      y = y + 1
      total = total + 1
   elif voto == 0:
      z = z + 1
      total = total + 1
   elif voto != 0 and voto != 93 and voto != 83 and voto != -1:
      w = w + 1
   if x > y:
      vencedor = 83
   else:
      vencedor = 93
   if (voto == -1):
      break
      
print(x)
print(y)
print(z)
print(w)
print(vencedor)
print('%.2f' % (x/total * 100))
print('%.2f' % (y/total * 100))