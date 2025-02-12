"""
49.	Faça um programa que mostre os n termos da Série a seguir:
o	  S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m. 
Imprima no final a soma da série.
"""
vezes = int(input('Digite o número de vezes: '))
numerador = 1
divisor = 1
total = 0

for i in range(vezes):
  print(f'Termos {i}: {numerador}/{divisor}')
  total += (numerador / divisor)
  numerador += 1
  divisor += 2

print(f'Soma final: {total:.2f}')