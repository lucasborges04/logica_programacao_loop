"""
38.	Um funcionário de uma empresa recebe aumento salarial anualmente:
Sabe-se que:
 .	Esse funcionário foi contratado em 1995, com salário inicial de
 R$ 1.000,00;
a.	Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
b.	A partir de 1997 (inclusive), os aumentos salariais sempre correspondem
ao dobro do percentual do ano anterior.
Faça um programa que determine o salário atual desse funcionário.
Após concluir isto, altere o programa permitindo que o usuário digite o
salário inicial do funcionário.
"""

salario_inicial = float(input('Informe o salário: '))
salario_final = salario_inicial * 1.015
ano = 1995
aumento = 1.5

for i in range(ano, 2001):
    aumento *= 2
    salario_final *= (aumento / 100 + 1)
print(f'Em {i} o salário é de R${salario_final:.2f}')