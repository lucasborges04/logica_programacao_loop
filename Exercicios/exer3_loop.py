"""
Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.
"""
cont = 1
print('Números ímpares:')

while(cont <= 50):
    if(cont % 2 == 1):
        print(cont)
    cont += 1