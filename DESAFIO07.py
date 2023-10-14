#Faça um programa que leia um número de 0 a 9999 e motre na tela cada dígito separados por casa decimal.
numero = input('Digite seu numero : ')
numero=numero.replace('','0')
unidade = numero[-1]
dezena = numero[-2]
centena = numero[-3]
milhar = numero[-4]

print(f'Seu numero é: {numero}')
print(f'Sua unidade é: {unidade}')
print(f"Sua dezena é: {dezena}")
print(f"Sua centena é: {centena}")
print(f"Sua milhar é: {milhar}")