# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.
algo = input('digite algo: ')
print('O tipo primitivo desse valor é {} !'.format(type(algo)))
print('Só tem espaços? {}'.format(algo.isspace()))
print('É um número? {}'.format(algo.isnumeric()))
print('É alfabético? {}'.format(algo.isalpha()))
print('É alfanúmerico? {}'.format(algo.isalnum()))
print('Esta em maiúsculas? {}'.format(algo.isupper()))
print('Está em minúsculas? {}'.format(algo.islower()))
print('Está capitalizada? {}'.format(algo.istitle()))

#Faça um programa que leia um número e mostre seu antecessor e seu sucessor.
num = int(input('Digite um numero: '))
a=int(num-1)
s=int(num+1)
print('Seu numero é {0}, seu sucessor é {2} e seu antecessor é {1}'. format(num, a, s))

#Faça um programa que leia um número e mostre seu dobro, triplo e raiz quadrada.
import math
num=int(input('Digite um número: '))
d=num*2
t=num*3
r=math.sqrt(num)

print('O numero é {}, seu dobro é {}, seu triplo é {} e sua raiz quadrada é {}'.format(num, d, t, r))