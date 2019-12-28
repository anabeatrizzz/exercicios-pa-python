"""Desenvolva um programa que mostre na tela a soma dos 80 primeiros termos da serie: 1/6 + 2/7 + 3/8 + 4/9 + 5/10 + ..."""

soma = 0
for c in range(1, 80+1):
    soma = c / (c + 5)
print(f"A soma é {soma}")