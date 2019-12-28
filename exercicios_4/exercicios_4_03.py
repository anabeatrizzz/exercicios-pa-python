"""Escreva um programa que leia uma matriz (3x5 ou 5x3) de 15 números
inteiros e exiba ao final a soma dos valores de cada linha que
estão armazenados nesta matriz."""

matriz = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
valores = 0
for l in range(0, 3):
	for c in range(0, 5):
		matriz[l][c] = int(input(f'Linha {l} Coluna {c}'))

print()

print(f'{matriz[0][0]}', f'{matriz[0][1]}', f'{matriz[0][2]}')
print(f'{matriz[0][3]}', f'{matriz[0][4]}', f'{matriz[1][0]}')
print(f'{matriz[1][1]}', f'{matriz[1][2]}', f'{matriz[1][3]}')
print(f'{matriz[1][4]}', f'{matriz[2][0]}', f'{matriz[2][1]}')
print(f'{matriz[2][2]}', f'{matriz[2][3]}', f'{matriz[2][4]}')

print()

print(f'Soma dos numeros da primeira linha: {matriz[0][0] + matriz[0][1] + matriz[0][2]}')
print(f'Soma dos numeros da primeira linha: {matriz[0][3] + matriz[0][4] + matriz[1][0]}')
print(f'Soma dos numeros da primeira linha: {matriz[1][1] + matriz[1][2] + matriz[1][3]}')
print(f'Soma dos numeros da primeira linha: {matriz[1][4] + matriz[2][0] + matriz[2][1]}')
print(f'Soma dos numeros da primeira linha: {matriz[2][2] + matriz[2][3] + matriz[2][4]}')