"""Escreva um programa que leia 15 números inteiros e exiba na tela ao final, o maior número que foi digitado pelo usuário."""

maior = 0
for c in range(1, 15+1):
	n = int(input('Digite um numero: '))
	if c == 1 or n > maior:
		maior = n
print(f'\nMaior numero digitado: {maior}')
