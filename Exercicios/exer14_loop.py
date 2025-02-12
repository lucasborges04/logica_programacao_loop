"""
25.	Faça um programa que peça para n pessoas a sua idade, ao final o
programa devera verificar se a média de idade da turma varia entre 0 e 25,
26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa,
conforme a média calculada.
"""
n_pessoas = int(input('Digite o número de pessoas que irá informar a idade: '))
soma = 0

for i in range(1, n_pessoas + 1):
    idade = int(input(f'Informe a {i}º idade: '))
    soma += idade

media_idade = soma / n_pessoas

if(0 < media_idade <= 25):
    print(f'Essa turma é jovem! Média da idade: {media_idade}.')
elif(media_idade <= 60):
    print(f'Essa turma é adulta! Média da idade: {media_idade}.')
else:
    print(f'Essa turma é idosa! Média da idade: {media_idade}.')