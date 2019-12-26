# Escreva um programa que leia um valor em Reais (R$), leia também a cotação do Dólar,
# realize o cálculo da conversão de moeda (de Reais para Dólares) e exiba na tela o resultado.

real = float(input("Digite um valor em R$: "))
dolar = real / 4.09
print(f'O seu valor convertido em dolares é: {dolar:.2f}')
