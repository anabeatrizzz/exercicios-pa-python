"""Desenvolva um programa que mostre na tela a soma dos 100 primeiros termos da serie: 1 + 1/4 + 1/9 + 1/16 + 1/25 + ..."""

s = 0
for c in range(1, 100+1):
    s = 1 / c ** 2
print(f"A soma é {s}")