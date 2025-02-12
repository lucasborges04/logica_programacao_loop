"""
Faça um programa que, dado um conjunto de N números, determine o menor valor,
o maior valor e a soma dos valores.
"""
t_seq = int(input('Digite o tamanho da sequência: '))
maior = int(input(f'Digite o primeiro número: '))
menor = maior
soma = maior
cont = 1

while(cont < t_seq):
    num = int(input(f'Digite o {cont + 1}º número: '))
    if(num > maior):
        maior = num
    elif(num < menor):
        menor = num
    
    soma += num
    cont += 1

print(f'Maior número: {maior}.')
print(f'Menor: {menor}.')
print(f'Soma: {soma}.')