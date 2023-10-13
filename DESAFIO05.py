#Faça um algoritimo que leia o salário de um empregado e mostre como ficou após um aumento de 15%.
salario=float(input('Digite seu salário: R$'))
aumento=salario+(salario*0.15)
print(f'O seu salário é R${salario} e passará a ganhar R${aumento} com um aumento de 15%.')

# Escreva um programa que leia uma temperatura em ºc e converta diretamente para ºF.
tempc=float(input(' Digite uma temperatura em ºC : '))
tempf=(tempc*1.8)+32
print(f'A temperatura fica {tempf:.2f}ºF')

# Escreva um programa que leia a quantd de km percorridos por um carro alugado e a quantd de dias pelos quais foi alugado. Calcule o preço a pagar. R$60,00 por dia e R$0,15 pro km rodado.
dias=float(input(' Digite a qntd de dias alugados: '))
dias=dias*60
km=float(input(' Digite qnts km rodados: '))
km=km*0.15
total=dias+km
print(f'O total a pagar será R${total}')