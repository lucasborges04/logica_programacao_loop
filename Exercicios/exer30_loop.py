"""
Faça um programa que peça um numero inteiro positivo e em seguida mostre
este numero invertido.
o	Exemplo:
o	  12376489
  => 98467321
"""
num = int(input('Digite um número maior que 10: '))
aux = num
invertido = 0

while(aux != 0):
    invertido = invertido * 10 + aux % 10
    aux //= 10

print(f'Inverso de {num} = {invertido}')
