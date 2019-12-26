"""Escreva um programa que exiba todos os números de 1 a 100 e a cada número que for múltiplo de 10,
exiba a mensagem “MÚLTIPLO DE 10”."""

for c in range(1, 100+1):
	if c % 10 == 0:
		print(f'{c} Múltiplo de 10')
	else:
		print(c)
