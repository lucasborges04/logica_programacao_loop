"""
Faça um programa que calcule o fatorial de um número inteiro fornecido pelo
usuário. Ex.: 5!=5.4.3.2.1=120
"""
num = int(input('Digite um número para calcular o fatorial: '))
cont = 1
fatorial = 1

while(cont <= num):
    fatorial *= cont
    cont += 1
print(f'{num}! = {fatorial}')