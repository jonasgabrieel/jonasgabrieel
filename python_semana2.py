#Volume da esfera
raio = float(input())
pi = 3.1416
volume = (4 * pi * raio ** 3) / 3

print('%.2f' %volume)

#Conta de luz, valor a ser pago e valor com desconto de 10%
kwh = float(input())
consumo = kwh * 1.50
desconto = consumo - consumo * 0.15

print('Valor a ser pago: R$','%.2f' %consumo ,'reais')
print('Valor a ser pago com desconto: R$','%.2f' %desconto ,'reais')

#Valor da agua, valor do esgoto e total
entrada = input()
valores = entrada.split()
Metros3 = float(valores[0])
ValorDagua= float (valores[1])


agua = Metros3 * 1000 * ValorDagua
esgoto = agua * 0.80
total = agua + esgoto

print('%.2f' %agua)
print('%.2f' %esgoto)
print('%.2f' %total)

#Area do triangulo,circulo,trapezio,quadrado e retangulo
entrada = input()
valores = entrada.split()
pi = 3.14159
A = float (valores[0])
B = float (valores[1])
C = float (valores[2])
TRIANGULO = A * C /2
CIRCULO = pi * C **2
TRAPEZIO = (A + B)*C /2
QUADRADO = B * B
RETANGULO = A * B


print('TRIANGULO:','%.3f' %TRIANGULO)
print('CIRCULO:','%2.3f' %CIRCULO)
print('TRAPEZIO:','%.3f' %TRAPEZIO)
print('QUADRADO:','%2.3f' %QUADRADO)
print('RETANGULO:','%2.3f' %RETANGULO)

#calcular menor número de notas possíveis (cédulas) no qual o valor pode ser decomposto
valor = int(input())
N = (0 < valor < 100000)


nota100 = (valor // 100)
nota50  = (valor % 100) // 50
nota20  = ((valor % 100 ) % 50) // 20
nota10  = (((valor % 100 ) % 50) % 20) // 10
nota5   = ((((valor % 100 ) % 50) % 20) %10) // 5
nota2   = (((((valor % 100 ) % 50) % 20) % 10) % 5) // 2                
nota1   = ((((((valor % 100 ) % 50) % 20) % 10) % 5) % 2) // 1

print(valor)
print(nota100,'nota(s) de R$ 100,00')
print(nota50,'nota(s) de R$ 50,00')
print(nota20,'nota(s) de R$ 20,00')
print(nota10,'nota(s) de R$ 10,00')
print(nota5,'nota(s) de R$ 5,00'  )
print(nota2,'nota(s) de R$ 2,00')
print(nota1,'nota(s) de R$ 1,00')

#Transformando um valor em segundos em horas minutos e segundos
seg = int (input())

hora    = seg // 3600
minuto  = (seg % 3600) // 60
segundo = (seg % 3600) - (minuto * 60)


print(str(hora) + ':' + str(minuto) + ':' + str(segundo))

#Converter uma temperatura dada em graus Fahrenheit para graus Celsius.
temperatura_far = float(input())
temperatura_cel = (temperatura_far - 32) / 1.8

print('%.2f' %temperatura_cel)

#Calcule o consumo médio de um automóvel sendo fornecidos a distância total percorrida (em Km) e o total de combustível gasto (em litros).
distancia = int(input())
consumo = float (input())


consumo_medio = distancia / consumo

print('%.3f' %consumo_medio , 'km/l')

