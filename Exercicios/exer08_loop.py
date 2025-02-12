"""
A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,...
Faça um programa capaz de gerar a série até o n-ésimo termo.
"""
n_termo = int(input('Digite o número da série desejada: '))
num1 = 1
num2 = 1
cont = 2
print(f'{num1}')
while(cont < n_termo):
    soma = num1 + num2
    num1 = num2
    num2 = soma
    cont += 1
print(soma)