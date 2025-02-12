"""
Altere o programa anterior para que ele aceite apenas números entre 0 e 1000
"""

t_seq = int(input('Digite o tamanho da sequência: '))
aceita = False

while(aceita != True):
    maior = int(input(f'Digite o primeiro número: '))
    menor = maior
    if(0 < maior < 1000):
        aceita = True
    else:
        print(f'Opção inválida! Digite um número entre 0 e 1000.')

soma = maior
cont = 1

while(cont < t_seq):
    aceita = False
    while(aceita != True):
        num = int(input(f'Digite o {cont + 1}º número: '))
        if(0 < num < 1000):
            aceita = True
        else:
            print(f'Opção inválida! Digite um número entre 0 e 1000.')
    if(num > maior):
        maior = num
    elif(num < menor):
        menor = num
    
    soma += num
    cont += 1

print(f'Maior número: {maior}.')
print(f'Menor: {menor}.')
print(f'Soma: {soma}.')