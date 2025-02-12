"""
27.	Faça um programa que calcule o número médio de alunos por turma.
Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma.
As turmas não podem ter mais de 40 alunos.
"""
qtd_turmas = int(input('Digite a quantidade de turmas: '))
soma = 0

for i in range(1, qtd_turmas + 1):
    verif = False
    while(verif != True):
        qtd_alunos = int(input(f'Digite a quantidade de alunos da turma {i}: '))
        if(0 < qtd_alunos < 40):
            soma += qtd_alunos
            verif = True
        else:
            print(f'Cada turma pode ter no máximo 40 alunos! Tente novamente.')
    
media = soma / qtd_turmas
print(f'Cada turma tem em média {media} alunos.')