#Escreva uma função chamada ClassificaAluno que receba como entrada a media e a quantidade de faltas de um aluno e retorne sua situação ao final do semestre.

media = float(input())
faltas = int(input())

def ClassificaAluno (media,faltas):
    if media > 9.5 and faltas < 10:
     return('APROVADO COM LOUVOR')
    elif media >= 7 and faltas < 10:
     return('APROVADO')
    elif media < 7:
     return('REPROVADO')
    elif faltas > 10:
     return('REPROVADO POR FALTAS')
    elif media == 7 and faltas == 10:
     return('APROVADO')

print(ClassificaAluno(media,faltas))

#Faça um programa que leia quatro notas (valores reais) de um aluno, calcule sua média ponderada utilizando, respectivamente, os pesos 1, 2, 3 e 4 para cada nota e imprima uma mensagem dizendo se o aluno foi aprovado com louvor, aprovado, reprovado ou deverá fazer prova final. Na sua solução utilize uma função chamada AnalisarSituacao




entrada = input()
valores = entrada.split()
nota1   = float(valores[0])
nota2   = float(valores[1])
nota3   = float(valores[2])
nota4   = float(valores[3])
media   = ((1*nota1 )+ (2*nota2)+(3*nota3)+(4*nota4))//10

def AnalisarSituacao(nota1,nota2,nota3,nota4):
 if media >= 9:
  return('aprovado com louvor')
 elif media >=7:
  return('aprovado')
 elif media < 3:
  return('reprovado')
 elif media >=3 and media < 7:
  return('prova final')
print(AnalisarSituacao(nota1,nota2,nota3,nota4))


#Faça um programa que leia três valores e apresente o maior dos três valores lidos seguido da mensagem “eh o maior”. 


entrada = input()
valores = entrada.split()
a = int(valores[0])
b = int(valores[1])
c = int(valores[2])


def maior3(a,b,c):
 if a > b and a > c:
  return(a)
 elif b > a and b > c:
  return(b)
 else:
  return(c)

print(maior3(a,b,c),'eh o maior')


#Escreva um programa que identifique se os comprimentos dos lados fornecidos pelo usuário podem formar um retângulo.


l1 = int(input())
l2 = int(input())
l3 = int(input())
l4 = int(input())



def eRetangulo(l1,l2,l3,l4):
 if l1 == l2 and l3 == l4:
  return('RETANGULO')
 elif l2 == l3 and l1 == l4:
  return('RETANGULO')
 elif l1 == l3 and l2 == l4:
  return('RETANGULO')
 else:
  return('NAO EH UM RETANGULO')
  
print(eRetangulo(l1,l2,l3,l4))

#Escreva uma função chamada EstacaoAno que receba como entrada um dia e um mês e retorne o nome da estação correspondente.
 
 
dia = int(input())
mes = int(input())

def EstacaoAno(dia, mes):
    if mes in (1, 2):
        return 'VERAO'
    elif mes == 3:
        if dia < 21:
            return 'VERAO'
        else:
            return 'OUTONO'
    elif mes in (4, 5):
        return 'OUTONO'
    elif mes == 6:
        if dia < 21:
            return 'OUTONO'
        else:
            return 'INVERNO'
    elif mes in (7, 8):
        return 'INVERNO'
    elif mes == 9:
        if dia < 21:
            return 'INVERNO'
        else:
            return 'PRIMAVERA'
    elif mes in (10, 11):
        return 'PRIMAVERA'
    elif mes == 12:
        if dia < 21:
            return 'PRIMAVERA'
        else:
            return 'VERAO'
            
            
print(EstacaoAno(dia, mes))

#Elabore um programa que contenha uma função que receba como parâmetros: hemisfério, dia e mês e exiba a estação do ano correspondente.


hemisferio = int(input())
dia = int(input())
mes = int(input())

def EstacaoAnoSul(hemisferio,dia, mes):
  if hemisferio == 1:
    if mes in (1, 2):
        return 'VERAO'
    elif mes == 3:
        if dia < 21:
            return 'VERAO'
        else:
            return 'OUTONO'
    elif mes in (4, 5):
        return 'OUTONO'
    elif mes == 6:
        if dia < 21:
            return 'OUTONO'
        else:
            return 'INVERNO'
    elif mes in (7, 8):
        return 'INVERNO'
    elif mes == 9:
        if dia < 21:
            return 'INVERNO'
        else:
            return 'PRIMAVERA'
    elif mes in (10, 11):
        return 'PRIMAVERA'
    elif mes == 12:
        if dia < 21:
            return 'PRIMAVERA'
        else:
            return 'VERAO'


def EstacaoAnoNorte(hemisferio,dia, mes):
    EstacaoAnoSul = EstacaoAnoSul(hemisferio,dia,mes)
    if EstacaoAnoSul == 'PRIMAVERA':
        return 'OUTONO'
    elif EstacaoAnoSul == 'OUTONO':
        return 'PRIMAVERA'
    elif EstacaoAnoSul == ' INVERNO':
         return 'VERAO'
    elif EstacaoAnoSul == 'VERAO':
        return 'INVERNO'
if hemisferio   == 0:
 print(EstacaoAnoNorte(hemisferio,dia,mes))
elif hemisferio == 1:
 print(EstacaoAnoSul(hemisferio,dia,mes))

 # Menor vwlocidae final de três carros

 veloc_ini1 = float(input())
acel1      = float(input())
temp1      = float(input())
veloc_final1 = (veloc_ini1 + (acel1 * temp1))*3.6

veloc_ini2 = float(input())
acel2      = float(input())
temp2      = float(input())
veloc_final2 = (veloc_ini2 + (acel2 * temp2))*3.6

veloc_ini3 = float(input())
acel3      = float(input())
temp3      = float(input())
veloc_final3 = (veloc_ini3 + (acel3 * temp3))*3.6

def velkmh  (veloc_final1,veloc_final2,veloc_final3):
 if veloc_final1 < veloc_final2 and veloc_final1 < veloc_final3:
  return('%.2f' %veloc_final1)
 elif veloc_final2 < veloc_final1 and veloc_final2 < veloc_final3:
  return('%.2f' %veloc_final2)
 elif    veloc_final3 < veloc_final1 and  veloc_final3 < veloc_final2:
  return('%.2f' %veloc_final3)
  
print(velkmh (veloc_final1,veloc_final2,veloc_final3))

print(AnalisarSituacao(nota1,nota2,nota3,nota4))