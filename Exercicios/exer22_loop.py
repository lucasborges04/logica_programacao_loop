"""
35.	Encontrar números primos é uma tarefa difícil.
Faça um programa que gera uma lista dos números
primos existentes entre 1 e um número inteiro informado pelo usuário.
"""
num = int(input('Informe um número: '))
i = 2 #Começa com 2 porque 1 não é primo
print(f'Números primos entre 1 e {num}:')
while(i <= num):
    div = 0
    j = 1
    while(j <= i):
        if(i % j == 0):
            div += 1
        j += 1
    if(div == 2):
        print(f'{i}')
    
    i += 1