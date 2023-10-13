#Cria um programa que leia quanto voce tem na carteira em reais e retorne quanto voce pode comprar em dolár. ref: U$1.00 = R$ 3,27.
carteira=float(input('Quanto você tem na carteira? '))
dolar=carteira/3.27
print(f'Com R${carteira} você pode comprar U${dolar}')