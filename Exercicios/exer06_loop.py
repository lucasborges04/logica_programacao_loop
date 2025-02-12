"""
Faça um programa que peça dois números, base e expoente, calcule e mostre o
primeiro número elevado ao segundo número. Não utilize a função potência da
linguagem.
2**3 = (((1*2)*2)*2) = 8
2**4 = 1*2*2*2*2 = 16
2**0 = 1
"""
base = int(input('Digite o primeiro número: '))
expoente = int(input('Digite o segundo número: '))
resultado = 1
cont = 0

while(cont < expoente):
    resultado *= base
    cont += 1
print(f'{base} elevado {expoente} é igual a {resultado}')