"""
Faça um programa que leia 5 números e informe o maior número.
"""

cont = 1
maior = int(input('Digite um número: '))

while(cont < 5):
    num = int(input('Digite outro número: '))

    if(num > maior):
        maior = num
    
    cont += 1

print(f'O maior número é {maior}')