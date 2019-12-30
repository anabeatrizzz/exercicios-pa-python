"""Supondo que a população de um país A seja da ordem de 90.000.000 habitantes com uma taxa anual de crescimento de 3% e que a população de um país B seja aproximadamente de 200.000.000 habitantes com uma taxa anual de crescimento de 1,5%.
Fazer um algoritmo que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas essas taxas de crescimento."""

a = 90000000
b = 200000000
ano = 0
while a <= b:
	a *= 0.03
	b *= 0.015
	ano += 1
print(f"A quantidade de anos para A chegar até B é: {ano}")