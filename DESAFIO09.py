import random
#Jogo de Adivinhação
numero=random.randrange(0,5)
user=int(input('digite um numero: '))
if numero == user:
    print('Parabéns, voce acertou !!')
else:
    print('Sinto muito, voce errou!')

# radar de velocidade
velocidade=int(input('Qual foi a velocidade?: '))
multa=(velocidade-80)*7
if velocidade <= 80:
    print('Você está dentro do limite permitido !')
else:
    print(f'Você passou com {velocidade} e está acima do limite, sua multa será de R${multa}!')