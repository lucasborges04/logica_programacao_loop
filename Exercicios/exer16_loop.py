"""
28.	Faça um programa que calcule o valor total investido por um colecionador
em sua coleção de CDs e o valor médio gasto em cada um deles.
O usuário deverá informar a quantidade de CDs e o valor para em cada um.
"""
qtd_cd = int(input('Informe a quantidade de CDs: '))
total = 0

for i in range(1, qtd_cd + 1):
    valor_cd = float(input(f'Valor do {i}º CD: '))
    total += valor_cd
media = total / qtd_cd
print(f'Ao todo são {qtd_cd} CDs com um valor de investimento total de R${total:.2f}')
print(f'Foi gasto em média em cada CD R${media:.2f}.')