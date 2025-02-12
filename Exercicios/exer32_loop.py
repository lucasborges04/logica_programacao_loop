"""
50.	Sendo H= 1 + 1/2 + 1/3 + 1/4 + ... + 1/N,
Faça um programa que calcule o valor de H com N termos.
"""
termos = int(input('Informe o núemro de termos: '))
h = 0

for divisor in range (1, termos + 1):
    h += (1/divisor)
print(f'A soma é {h:.2f}')