"""Escreva um programa que exiba na tela em ordem crescente, apenas os números pares existentes de 11 a 250."""

imp = 0
for c in range(11, 250+1):
	if c % 2 != 0:
		imp = c
		print(imp)
