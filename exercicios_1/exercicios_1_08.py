# Escreva um programa que leia um valor em Reais (R$), leia também a cotação do Dólar e do Euro,
# realize o cálculo das respectivas conversões de moedas (de Reais para Dólares e de Reais para Euros)
# e exiba os resultados na tela.

real = float(input("Digite um valor em R$ "))
dolar = real / 4.09
euro = real / 4.54
print(f"Você tem {dolar:.2f} dolares")
print(f"Você tem {euro:.2f} euros")
