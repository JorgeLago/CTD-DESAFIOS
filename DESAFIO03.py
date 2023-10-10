#Faça um programa que leia duas notas de um aluno e dê a sua média
nota1=float(input('Qual a primeira nota?: '))
nota2=float(input('Qual a segunda nota?: '))
m=(nota1+nota2)/2
print('Sua média é {}'.format(m))

#Faça um programa que leia uma distancia em metros e converta em km, hm, dam, dm, cm, mm
distancia=int(input('Distancia em metro: '))
km=distancia/1000
hm=distancia/100
dam=distancia/10
dm=distancia*10
cm=distancia*100
mm=distancia*1000

print('A distancia de {} metros corresponde a {}km, {}hm, {}dam, {}dm, {}cm, {}mm'.format(distancia, km, hm, dam, dm, cm, mm))