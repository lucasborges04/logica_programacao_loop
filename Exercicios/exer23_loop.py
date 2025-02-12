"""
Peça para o usuario entrar com o ínicio e o fim da tabuada
e imprima a tabuada correspondente dentro dos intervalos considerados
Exemplo:
Começo = 1
Fim = 3

Para o 1:
1X1 = 1
1X2 = 2
1X3 = 3

Para o 2:
2X1 = 2
2X2 = 4
2X3 = 6

Para o 3:
3X1 = 3
3X2 = 6
3X3 = 9
"""
inicio = int(input('Entre com o início da tabuáda: '))
fim = int(input('Informe o final da tabuáda: '))

for i in range(inicio, fim + 1):
    print(f'\nTabuada do {i}:')
    for j in range(inicio, fim + 1):
        tabuada = i * j
        print(f'{i} x {j} = {tabuada}')