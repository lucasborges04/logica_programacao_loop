"""
Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o
fatorial várias vezes e limitando o fatorial a números inteiros positivos
e menores que 16.
"""
limitando = False

while(limitando != True):
    aceita = False
    while(aceita == False):
        num = int(input('Digite um número para saber seu fatorial: '))
        if(0 < num < 16):
            aceita = True
        else:
            print(f'Opção inválida! Digite um número entre 0 e 16.')
        
    aceita = True
    fatorial = 1
    cont = 1

    while(cont <= num):
        fatorial *= cont
        cont += 1

    print(f'{num}! = {fatorial}')

    acabou = bool(int(input('Deseja digitar mais um valor (1 - Sim/ 0 - Não): ')))
    if(acabou == 0):
        limitando = True