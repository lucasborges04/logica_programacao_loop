"""
24.	Faça um programa que calcule o mostre a média aritmética de N notas.
"""
n_notas = int(input('Digite a quantidade de notas que será informada: '))
cont = 1
soma_notas = 0

while(cont <= n_notas):
    nota = float(input(f'Digite sua {cont}º nota: '))
    soma_notas += nota
    cont += 1

media = soma_notas / n_notas
print(f'Média de {media:.2}.')