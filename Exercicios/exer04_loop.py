"""
4.	Supondo que a população de um país A seja da ordem de 80000 habitantes
com uma taxa anual de crescimento de 3% e que a população de B seja 200000
habitantes com uma taxa de crescimento de 1.5%.

Faça um programa que calcule e escreva o número de anos necessários para que a
população do país A ultrapasse ou iguale a população do país B, mantidas as
taxas de crescimento.
"""
pais1 = 80000
tx_cres1 = 1.20

pais2 = 200000
tx_cres2 = 1.015

cont = 0

while(pais1 <= pais2):
    reajuste1 = pais1 * tx_cres1
    reajuste2 = pais2 * tx_cres2
    cont += 1
print(f'Será necessário {cont} anos.')