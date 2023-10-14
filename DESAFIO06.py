import math
# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
num = float(input('Digite um número real: '))
num2 = math.trunc(num)
print(f'Seu numero é {num} e sua parte inteira é {num2}')

# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com toda a letras maiúcula e minúsculas, Quantas letras ao todo(sem contar os espaços), Quantas letras tem o primeiro nome.
nome = input('Digite seu nome completo: ')
maiusculas = nome.upper()
minusculas = nome.lower()
qntd = len(nome) - nome.count(' ')
primeiro = nome.split()
primeiro = len((primeiro[0]))
print(maiusculas)
print(minusculas)
print(qntd)
print(primeiro)
