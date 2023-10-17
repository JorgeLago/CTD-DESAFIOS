#Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
nome=input('Digite eu nome completo: ').upper().strip()
print('SILVA' in nome)

#Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
nome=str(input('Digite seu nome completo: ').upper().strip())
qntd=nome.count('A')
primeiro=nome.find('A')+1
ultimo=nome.rfind('A')+1
print(f'Seu nome tem {qntd} A.s !')
print(f'O primeiro aparece na posição {primeiro}')
print(f'O ultimo aparece na posição {ultimo}')

# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

print(f'O seu primeiro nome é: {primeironome}')
print(f'O seu ultimo nome é: {ultimonome}')