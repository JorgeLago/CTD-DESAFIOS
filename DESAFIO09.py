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

#Verificando de é par ou impar um numero.
numero=int(input('Digite seu numero: '))
n=numero%2
if n == 0:
    print('É Par o seu numero !!')
else:
    print(' É impar o seu numero !!')