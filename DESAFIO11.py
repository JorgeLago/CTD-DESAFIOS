#DESENVOLVER ALGORÍTIMO
# Diretor cadastra alunos com os dados:
# - nome, CPF, Email, Matrícula.
# Pra cada aluno cadastrado, o diretor poder lançar 3 notas
# Se a media atingida for maior ou igual a 6, escrever:
# Aluno X, voce foi aprovado. Seu diploma terá os seguintes dados.
#  Listar todos os dados daquele aluno
#caso a médiaseja inferior a 6. lançar uma nota adicional e tirar nova média.
# Senão, aluno reprovado.

aluno=input('Qual nome do aluno? ')
cpf=int(input('Qual o cpf do aluno? '))
email=input('Agora digite o email ')
matricula=input('Qual a matricula? ')
nota1=int(input('Primeira nota: '))
nota2=int(input('Segunda nota: '))
nota3=int(input('Terceira nota: '))
media=(nota1+nota2+nota3)/3
if media>=6:
    print(f'Aluno {aluno}, voce foi aprovado. Seu diploma terá os seguintes dados:')
elif media<=6:
    nota4=int(input('Digite a nota adicional: '))
    nova_media=(nota1+nota2+nota3+nota4)/4
else:
    print('Aluno está reprovado !')