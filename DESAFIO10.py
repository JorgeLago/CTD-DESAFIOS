#Calculando passagem do onibus
distance=int(input('Digite a distancia da viagem em km: '))
if distance <= 200:
    print(f'A sua passagem custará R${distance*0.50}!!')
else:
    print(f'A sua passagem custará R${distance*0.45}!!')

#