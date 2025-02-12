"""
39.	Faça um programa que leia dez conjuntos de dois valores,
o primeiro representando o número do aluno e o segundo representando a sua
altura em centímetros. Encontre o aluno mais alto e o mais baixo.
Mostre o número do aluno mais alto e o número do aluno mais baixo, junto com
suas alturas.
"""
numero = int(input('Qual seu número: '))
altura = int(input('Qual sua altura (cm): '))
alto = altura
baixo = alto
numero_alto = numero
numero_baixo = numero_alto

for i in range(1, 11):
    numero = int(input('\nDigite seu número: '))
    altura = int(input('Qual sua alturac(cm): '))
    if(altura > alto):
        alto = altura
        numero_alto = numero
    if(altura < baixo):
        baixo = altura
        numero_baixo = numero
print(f'O mais alto tem {alto}cm e seu número é {numero_alto}.')
print(f'O mais baixo tem {baixo}cm e seu número é {numero_baixo}.')