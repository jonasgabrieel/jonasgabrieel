#Tabuada
num = 5

print(num,'X 1 =', num*1 )
print(num,'X 2 =', num*2 )
print(num,'X 3 =', num*3 )
print(num,'X 4 =', num*4 )
print(num,'X 5 =', num*5 )
print(num,'X 6 =', num*6 )
print(num,'X 7 =', num*7 )
print(num,'X 8 =', num*8 )
print(num,'X 9 =', num*9 )


#Valor da conta somado aos 10% do garçom
valor = float(input())
percentual = (valor*10 / 100) + valor
print('%.2f' %percentual)

#Area do circulo
raio = float(input())
pi = 3.14159
area = raio ** 2 *pi /10000

print('Area =', '%.4f' % area)


#As quatro operaço~es matematicas entre dois numeros
nump = float(input())
nums = float(input())

print('%.2f' %(nump + nums))
print('%.2f' %(nump - nums))
print('%.2f' %(nump * nums))
print('%.2f' %(nump / nums))

#Salario e percentual de aumento de um funcionario
salario = float(input())
percentual = float(input())

reajuste = (percentual / 100 * salario) + salario

print('Seu salario teve aumento de','%.1f' %percentual, '%, passando de R$','%.1f' %salario, 'para R$', '%.1f' %(reajuste))

#Media aritimetica de duas notas
pnota = float(input())
snota = float(input())

media = (pnota + snota)/2
print('%.2f' % media)

