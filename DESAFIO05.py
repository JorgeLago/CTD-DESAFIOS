#Faça um algoritimo que leia o salário de um empregado e mostre como ficou após um aumento de 15%.
salario=float(input('Digite seu salário: R$'))
aumento=salario+(salario*0.15)
print(f'O seu salário é R${salario} e passará a ganhar R${aumento} com um aumento de 15%.')