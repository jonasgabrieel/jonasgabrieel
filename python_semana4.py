#meses do ano por extenso
meses = int(input())

if meses == 1:
 print('janeiro')
elif meses == 2:
 print('fevereiro')
elif meses == 3:
 print('marco')
elif meses == 4:
 print('abril')
elif meses == 5:
 print('maio')
elif meses == 6:
 print('junho')
elif meses == 7:
 print('julho')
elif meses == 8:
 print('agosto')
elif meses == 9:
 print('setembro')
elif meses == 10:
 print('outubro')
elif meses == 11:
 print('novembro')
elif meses == 12:
 print('dezembro')

else:
 print('invalido')

 #Preço de um produto com garantia estendida
 valor_produto = float(input())
garantia = int(input())

if garantia == 1:
 print('%.2f' %(valor_produto * 3 / 100 + valor_produto))
elif garantia == 2:
 print('%.2f' %(valor_produto * 5 / 100 + valor_produto))
elif garantia == 0:
 print('%.2f' %valor_produto)

 #Leia um valor inteiro N. Depois, imprima uma mensagem dizendo que se este valor for ímpar, par, positivo, negativo ou nulo.
 Num = int(input())
if Num > 0 and Num % 2 == 0:
 print('POSITIVO PAR')
elif Num < 0 and Num % 2 != 0:
 print('NEGATIVO IMPAR')
elif Num > 0 and Num % 2 != 0:
 print('POSITIVO IMPAR')
elif Num < 0 and Num % 2 == 0:
 print('NEGATIVO PAR')
 
else:
 print('NULO')

 #Zerinho ou um com 3 jogadores
alice = int(input())
beto  = int(input())
clara = int(input())

if clara == beto == alice:
 print('*') 
elif alice == beto and alice != clara:
 print('C')
elif clara == beto and clara != alice:
 print('A')
elif alice == clara and alice != beto:
 print('B')
 

 #Faça um programa que leia três notas de um aluno, calcule sua média aritmética e uma mensagem dizendo se o aluno foi aprovado, reprovado ou deverá fazer prova final.
Nota1 = float(input())
Nota2 = float(input())
Nota3 = float(input())
media = (Nota1 + Nota2 + Nota3) / 3


if media >= 7:
 print('aprovado')

elif media < 3:
 print('reprovado')

elif media >= 3 and media < 7 :
 print('prova final')


#Dados 3 numeros saber quantos são iguais
num1 = int(input())
num2 = int(input())
num3 = int(input())

if num1 == num2 and num1 == num3 :
 print(1)
 
elif num1 != num2 and num1 != num3 :
 print(2)
 
else:
 print(3)

#1 livro para até 8 alunos --> Conceito A
#1 livro para entre 9 e 12 alunos --> Conceito B
#1 livro para entre 13 e 18 alunos --> Conceito C
#1 livro para mais de 18 alunos --> Conceito D

livro = int(input())
aluno = int(input())
media = aluno / livro

if media <= 8:
 print('A')
elif media >= 9 and media <= 12:
 print('B')
elif media >= 13 and media <= 18:
 print('C')
elif media > 18:
 print('D')


 #Classificaçao dos triangulos
lado1 = float(input())
lado2 = float(input())
lado3 = float(input())
if lado1 == lado2 and lado1 == lado3:
 print('equilatero')
elif lado1 != lado2 and lado1 != lado3 and lado2 != lado3:
 print('escaleno')

else:
 print('isosceles')

 #Categoria de nadadores
idade = int(input())

if idade >= 5 and idade <= 7:
 print('Infantil A')
elif idade >= 5 and idade <=10:
 print('Infantil B')
elif idade >= 11 and idade <=13:
 print('Juvenil A')
elif idade >= 14 and idade <= 17:
 print('Juvenil B')
elif idade >= 18 and idade <= 40:
 print('Adulto')
elif idade >= 41:
 print('Master')
else:
 print('Idade invalida.')

 #Valor da conta de energia seguido do valor do kwh
kwh = int(input())
taxa1 = 1.35
taxa2 = 1.55
taxa3 = 1.75
taxa4 = 2.15


if kwh >= 1  and kwh <= 25:
 print('%.2f' % 35)
 print(taxa1)  
 
elif kwh >= 26 and kwh <= 99:
 print('%.2f' %(kwh * taxa1 ))
 print(taxa1)
    
elif kwh >= 100 and kwh <= 299:
 print('%.2f' %(kwh * taxa2 ))
 print(taxa2)
 
elif kwh >= 300 and kwh <= 574 :
 print('%.2f' %((kwh * taxa3 * 0.10) + kwh * taxa3 ))
 print(taxa3)
 
elif kwh >= 575:
 print('%.2f' %((kwh * taxa4 * 0.10) + kwh * taxa4 ))
 print(taxa4)
 