"""
Faça um programa que leia uma quantidade indeterminada de números positivos e
conte quantos deles estão nos seguintes intervalos: [0-25], [26-50], [51-75] e
[76-100].
A entrada de dados deverá terminar quando for lido um número negativo.
"""
num = int(input('Digite um número (-1 para sair): '))
de0_25 = 0
de26_50 = 0
de51_75 = 0
de76_100 = 0

while(num >= 0):
    if(0 <= num <= 25):
        de0_25 += 1
    elif(num <= 50):
        de26_50 += 1
    elif(num <= 75):
        de51_75 += 1
    elif(num <= 100):
        de76_100 += 1

    num = int(input('Digite um número (-1 para sair): '))

print(f'Temos {de0_25} número(s) no intervalo de [0 - 25].')
print(f'Temos {de26_50} número(s) no intervalo de [26 - 50].')
print(f'Temos {de51_75} número(s) no intervalo de [51 - 75].')
print(f'Temos {de76_100} número(s) no intervalo de [76 - 100].')