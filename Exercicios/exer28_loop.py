"""
43.	O cardápio de uma lanchonete é o seguinte:
o	Especificação   Código  Preço
o	Cachorro Quente 100     R$ 1,20
o	Bauru Simples   101     R$ 1,30
o	Bauru com ovo   102     R$ 1,50
o	Hambúrguer      103     R$ 1,20
o	Cheeseburguer   104     R$ 1,30
o	Refrigerante    105     R$ 1,00
Faça um programa que leia o código dos itens pedidos e as quantidades desejadas.
Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total
geral do pedido. Considere que o cliente deve informar quando o pedido deve
ser encerrado.
"""
encerrar = False
total = 0

while(encerrar != True):
    codigo = int(input('\nInsira o código do produto: '))
    qtd = int(input('Quantos você deseja comprar: '))
    if(codigo == 100):
        preco = qtd * 1.20
        total += preco
        especificacao = 'cachorro(s) quente(s)'
    elif(codigo == 101):
        preco = qtd * 1.3
        total += preco
        especificacao = 'bauru simples'
    elif(codigo == 102):
        preco = qtd * 1.5
        total += preco
        especificacao = 'bauru com ovo(s)'
    elif(codigo == 103):
        preco = qtd * 1.2
        total += preco
        especificacao = 'hambúrguer(s)'
    elif(codigo == 104):
        preco = qtd * 1.3
        total += preco
        especificacao = 'cheeseburguer(s)'
    elif(codigo == 105):
        preco = qtd * 1.0
        total += preco
        especificacao = 'refrigerante(s)'

    print(f'Foi adicionado {qtd} {especificacao} na lisa, saindo por R${preco}')

    sair = int(input(f'Deseja encerrar o pedido (1 - Sim/ 0 - Não): '))
    if(sair == 1):
        encerrar = True

print(f'Sua compra deu R${total}')
