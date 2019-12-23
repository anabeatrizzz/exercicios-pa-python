nota = soma = media = 0
for c in range(1, 10+1):
	nota = float(input(f'Escreva a {c}a nota: '))
	while nota < 0 or nota > 10:
		nota = float(input(f'Nota invalida, reecreva a {c}a nota'))
	soma += nota
media = soma / 10
print(f'\nA sua média é {media}')