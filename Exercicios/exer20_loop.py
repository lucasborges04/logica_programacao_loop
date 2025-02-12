"""
33.	O Departamento Estadual de Meteorologia lhe contratou para desenvolver
um programa que leia as um conjunto indeterminado de temperaturas, e informe
ao final a menor e a maior temperaturas informadas, bem como a média das
temperaturas.
"""
num = int(input('Informe a quantidade de temperaturas registrada: '))
maior = float(input(f'Temperatura 1: '))
menor = maior
total = 0

for i in range (2, num + 1):
    temp = float(input(f'Temperatura {i}: '))
    total += temp
    if(temp > maior):
        maior = temp
    elif(temp < menor):
        menor = temp
    
media = total / num
print(f'Maior temperatura: {maior}°C')
print(f'Menor temperatura: {menor}°C')
print(f'Média das temperaturas: {media:.1f}°C')