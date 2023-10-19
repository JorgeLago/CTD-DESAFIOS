import random
#Jogo de Adivinhação
numero=random.randrange(0,5)
user=int(input('digite um numero: '))
if numero == user:
    print('Parabéns, voce acertou !!')
else:
    print('Sinto muito, voce errou!')