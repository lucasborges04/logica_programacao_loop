"""
Faça um programa que peça 10 números inteiros, calcule e
mostre a quantidade de números pares e a quantidade de números impares.
"""
cont = 1
par = 0
impar = 0

while(cont <= 10):
    num = int(input(f'Digite o {cont}º número: '))
    if(num % 2 == 0):
        par += 1
    else:
        impar += 1
    
    cont += 1

print(f'Temos {par} número(s) par(es).')
print(f'Temos {impar} número(s) ímpar(es).')