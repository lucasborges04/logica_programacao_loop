"""
37.	Uma academia deseja fazer um senso entre seus clientes para descobrir
o mais alto, o mais baixo, a mais gordo e o mais magro, para isto você deve
fazer um programa que pergunte a cada um dos clientes da academia seu código,
sua altura e seu peso. O final da digitação de dados deve ser dada quando o
usuário digitar 0 (zero) no campo código. Ao encerrar o programa também deve
ser informados os códigos e valores do clente mais alto, do mais baixo, do
mais gordo e do mais magro, além da média das alturas e dos pesos dos clientes
"""
codigo = int(input(f'Informe seu código da academia (0 - Sair): '))
if(codigo != 0):
    altura = int(input('Informe sua altura (cm): '))
    maior_alt = altura
    menor_alt = maior_alt
    soma_alt = 0

    peso = float(input('Informe seu peso: '))
    gordo = peso
    magro = peso
    soma_peso = 0

    cont = 1

    while(codigo != 0):
        altura = int(input('\nInforme sua altura (cm): '))
        peso = float(input('Informe seu peso: '))
        codigo = int(input(f'Informe seu código da academia (0 - Sair): '))      
        
        if(altura > maior_alt):
            maior_alt = altura
        if(altura < menor_alt):
            menor_alt = altura
        if(peso > gordo):
            gordo = peso
        if(peso < magro):
            magro = peso
        cont += 1
    else:
        verif = False
    
    soma_alt += altura
    soma_peso += peso

media_alt = soma_alt / cont
media_peso = soma_peso / cont

print(f'Mais gordo: {gordo:.2f}kg.')
print(f'Mais magro: {magro:.2f}kg.')
print(f'Mais alto: {maior_alt}cm.')
print(f'Mais baixo: {menor_alt}cm.')
print(f'Média de altura: {media_alt:.2f}cm.')
print(f'Média de peso: {media_peso:.2f}kg.')


        
soma_alt += altura