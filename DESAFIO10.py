#Calculando passagem do onibus
distance=int(input('Digite a distancia da viagem em km: '))
if distance <= 200:
    print(f'A sua passagem custará R${distance*0.50}!!')
else:
    print(f'A sua passagem custará R${distance*0.45}!!')

#Faça um programa que leia um ano e mostre se ele é BISSEXTO!.
ano=int(input(' Digite um ano a ser verificado: '))
verifica=ano%4
if verifica == 0:
    print('Esse ano é Bissexto !')
else:
    print('Esse ano não é Bissexto !')

#Faça um programa que leia 3 numeros e mostre qua o maior e qual o menor.
num1=int(input('Digite o primeiro numero: '))
num2=int(input('Digite o segundo numero: '))
num3=int(input('Digite o terceiro numero: '))
print(f'O menor numero é {min(num1,num2,num3)} e o maior numero é {max(num1,num2,num3)} !!')
#Escreva um programa que leia um salario e mostre seu aumento. se for mais que 1250 tem aumento de 10%, se for menor igual 15%.
salario=float(input('Digite o valor do salário: '))
if salario <= 1250:
    print(f'Seu salario anterior é R${salario} e passará a ser R${salario+(salario*0.15)}')
else:
    print(f'Seu salario será {salario+(salario*0.10)}')

#Faça um programa que leia 3 comprimentos de retas e diga se podem ser um triangulo ou nao.
lado1=float(input('Digite o comprimento do primeiro lado: '))
lado2=float(input('Digite o comprimento do segundo lado: '))
lado3=float(input('Digite o comprimento do terceiro lado: '))
if lado1 < lado2+lado3 and lado2 < lado1+lado3 and lado3 < lado1+lado2:
    print('Pode ser um triângulo!')
else:
    print('Não forma um triangulo!')