"""
Os números primos possuem várias aplicações dentro da Computação,
por exemplo na Criptografia. Um número primo é aquele que é divisível
apenas por um e por ele mesmo.
Faça um programa que peça um número inteiro e determine se ele é ou não
um número primo.
"""
num = int(input('Informe o número: '))

if(num > 1):
    div = 0
    
    for i in range(1, num + 1):
        if(num % i == 0):
            div += 1
    
    if(div == 2):
        print(f'{num} é número primo!')
    else:
        print(f'{num} não é número primo!')

else:
    print(f'{num} não é número primo!')