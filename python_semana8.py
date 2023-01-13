#entrada de cpf
entrada = input()
terno1 = entrada[0:3]
terno2 = entrada[4:7]
terno3 = entrada[8:11]
terno4 = entrada[12:14]


print(terno1)
print(terno2)
print(terno3)
print(terno4)

#Soma de digitos 
string = input()


def SomaDigito(num):
   soma = 0
   for num in string:
    soma = soma + int(num)
   return soma
print(SomaDigito(string))
 
#palindromo
num = int(input())
for item in range(num):
    comeco = ''
    palavra = input().lower()
    for char in palavra:
        if char != " ":
            comeco += char
    if comeco == comeco[::-1]:
        print("SIM")
    else:
        print("NAO")

#inverter string
string = input()

def Inverter(string):
  return string[::-1]
  
print(Inverter(string))


#contar um caracter na string
string = input()
caracter = input() 
def contador (string,caracter):
 return string.count(caracter)
  
print(contador(string,caracter))

#Ultima palavra da frase

string = input().split()
print(string[-1])

#Penultima letra de uma palavra

string = input()

def inverter(string):
  return string[::-1]
def frase (inverter):
  return string[-2]

print(inverter(string))
print(frase(inverter))