"""
Implemente um jogo básico do clássico “Jogo da Velha”.
Onde deverá ser usada uma matriz 3x3.
Dicas: Para identificar o jogador, utilizar uma variável que servirá como um contador,
e para contador sendo par associa-se a jogada sendo do jogador 1, senão, em caso de ímpar associa-se ao jogador 2.
A matriz pode ser do tipo char para armazenar ‘O’ e ‘X’, ou também do tipo int para armazenar 1 e 2,
identificando o número do jogador.
"""

import os
import time

def Desenho(matriz):
	print(f"  {matriz[0][0]}  |  {matriz[0][1]}  |  {matriz[0][2]}")
	print(f"_____ _____ _____")
	print(f"  {matriz[1][0]}  |  {matriz[1][1]}  |  {matriz[1][2]}")
	print(f"_____ _____ _____")
	print(f"  {matriz[2][0]}  |  {matriz[2][1]}  |  {matriz[2][2]}")


def Vitoria(m):
	if m[0][0] == m[0][1] == m[0][2]:
		return 1
	elif m[1][0] == m[1][1] == m[1][2]:
		return 1
	elif m[2][0] == m[2][1] == m[2][2]:
		return 1
	elif m[0][0] == m[1][0] == m[2][0]:
		return 1
	elif m[0][1] == m[1][1] == m[2][1]:
		return 1
	elif m[0][2] == m[1][2] == m[2][2]:
		return 1
	elif m[0][0] == m[1][1] == m[2][2]:
		return 1
	elif m[0][2] == m[1][1] == m[2][0]:
		return 1
	elif m[0][0] != '0' and m[0][1] != '1' and m[0][2] != '2' and m[1][0] != '3' and m[1][1] != '4' and m[1][2] != '5' and m[2][0] != '6' and m[2][1] != '7' and m[2][2] != '8':
		return -1
	else:
		return 0

cont = 1
verifica = 0
matriz = [['0','1','2'], ['3','4','5'], ['6','7','8']]

while -1 != verifica != 1:
	clear = lambda: os.system('clear')
	clear()
	print("----- Jogo da Velha -----\n")
	print("Jogador 1: X\nJogador 2: O\n")
	Desenho(matriz)
	cont += 1
	if cont % 2 == 0:
		print("\nVez do jogador 1.")
	if cont % 2 == 1:
		print("\nVez do jogador 2.")
	posicao = int(input("Escolha sua posição: "))
	linha = posicao // 3
	coluna = posicao % 3
	if matriz[linha][coluna] != 'X' and matriz[linha][coluna] != 'O':
		if cont % 2 == 0:
			matriz[linha][coluna] = 'X'
			Desenho(matriz)
		elif cont % 2 == 1:
			matriz[linha][coluna] = 'O'
			Desenho(matriz)
		else:
			print(f"Desculpe, a linha {posicao} já está marcada com {matriz[linha][coluna]}")
			print("Por favor, espere 3 segundos, o jogo da velha está carregando...")
			time.sleep(3)
		verifica = Vitoria(matriz)
clear = lambda: os.system('clear')
clear()
Desenho(matriz)
if verifica == 1:
	print(f"\nO jogador {(cont % 2) + 1} ganhou")
else:
	print("\nDeu velha!")
