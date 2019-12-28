"""Desenvolva um programa que mostre na tela a soma dos primeiros 123 termos da serie: 1/6 + 2/3 + 3/4 + 4/5 ... + 123/124"""

s = 0
for c in range(1, 123+1):
	s = c // (c + 1)
print(f"A soma é {s}")