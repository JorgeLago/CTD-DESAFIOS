#Cria um programa que leia quanto voce tem na carteira em reais e retorne quanto voce pode comprar em dolár. ref: U$1.00 = R$ 3,27.
carteira=float(input('Quanto você tem na carteira? '))
dolar=carteira/3.27
print(f'Com R${carteira} você pode comprar U${dolar:.2f}')

#Faça um programa que leia a largura e a altura de uma parede em metros. calcule a area  e a quantidade de tinta necessária para pintar. sabendo que cada litro de tinta, pinta uma área de 2m².
altura=float(input('Digite a altura: '))
largura=float(input('Digite a largura: '))
parede=altura*largura
litros=parede/2
print(f'sua parede tem {parede}m² de área e precisa de {litros:.2f}l para pintar toda')

#