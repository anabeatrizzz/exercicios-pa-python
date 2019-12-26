"""Escreva um programa que calcule e exiba a média de 10 notas digitadas pelo usuário.
Considerar notas válidas, somente valores entre 0 (zero) e 10 (dez).
Se o usuário digitar algum valor inválido, deverá ser exibida uma mensagem informando o ocorrido."""

nota = soma = media = 0
for c in range(1, 10+1):
	nota = float(input(f'Escreva a {c}a nota: '))
	while nota < 0 or nota > 10:
		nota = float(input(f'Nota invalida, reecreva a {c}a nota'))
	soma += nota
media = soma / 10
print(f'\nA sua média é {media}')
