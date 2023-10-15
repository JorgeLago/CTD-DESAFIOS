# Faça um programa que leia um número de 0 a 9999 e motre na tela cada dígito separados por casa decimal.
numero = int(input('Digite seu numero : '))
unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10

print(f'Seu numero é: {numero}')
print(f'Sua unidade é: {unidade}')
print(f"Sua dezena é: {dezena}")
print(f"Sua centena é: {centena}")
print(f"Sua milhar é: {milhar}")
