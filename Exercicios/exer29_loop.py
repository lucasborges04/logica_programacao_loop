"""
44.	Em uma eleição presidencial existem quatro candidatos. Os votos são
informados por meio de código. Os códigos utilizados são:
o	1 , 2, 3, 4  - Votos para os respectivos candidatos 
o	(você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
o	5 - Voto Nulo
o	6 - Voto em Branco
Faça um programa que calcule e mostre:
o	O total de votos para cada candidato;
o	O total de votos nulos;
o	O total de votos em branco;
o	A percentagem de votos nulos sobre o total de votos;
o	A percentagem de votos em branco sobre o total de votos.
Para finalizar o conjunto de votos tem-se o valor zero.
"""
eleicao = True
v_joao = 0
v_jair = 0
v_celina = 0
v_bastos = 0
v_nulos = 0
v_branco = 0
total = 0

while(eleicao):
    print(f'\n1 - João')
    print(f'2 - Jair')
    print(f'3 - Celina')
    print(f'4 - Bastos')
    print(f'5 - Voto Nulo')
    print(f'6 - Voto em Branco')
    print(f'0 - Finalizar')

    voto = int(input('\nInsira seu voto: '))
    if(voto == 1):
        v_joao += 1
        total += 1
    elif(voto == 2):
        v_jair += 1
        total += 1
    elif(voto == 3):
        v_celina += 1
        total += 1
    elif(voto == 4):
        v_bastos += 1
        total += 1
    elif(voto == 5):
        v_nulos += 1
        total += 1
    elif(voto == 6):
        v_branco += 1
        total += 1
    elif(voto == 0):
        eleicao = False

per_nulos = (v_nulos / total) * 100
per_branco = (v_branco / total) * 100

print(f'\nTotal de votos: {total}')
print(f'Votos do João: {v_joao}')
print(f'Votos do Jair: {v_jair}')
print(f'Votos da Celina: {v_celina}')
print(f'Votos do Bastos: {v_bastos}')
print(f'Votos Nulo: {v_nulos}. Equivalente a {per_nulos:.2f}% dos votos.')
print(f'Votos em Branco: {v_branco}. Equivalente a {per_branco:.2f}% dos votos.\n')