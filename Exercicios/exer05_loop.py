"""
Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número
inteiro entre 1 a 10. O usuário deve informar de qual numero ele deseja ver a
tabuada. A saída deve ser conforme o exemplo abaixo:
o	Tabuada de 5:
o	5 X 1 = 5
o	5 X 2 = 10
o	...
o	5 X 10 = 50
"""
tabuada = int(input('Digite o número da tabuáda que você deseja: '))
cont = 1
print(f'Tabuada do {tabuada}:\n')

while(cont <= 10):
    mult = tabuada * cont
    print(f'{tabuada} X {cont} = {mult}')
    cont += 1
