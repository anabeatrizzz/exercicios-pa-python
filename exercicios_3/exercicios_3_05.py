"""Escreva um programa que exiba o seguinte menu
e crie um método para realizar os cálculos de cada item deste menu:
1 – Soma
2 – Subtração
3 – Divisão
4 – Multiplicação
5 – Resto da Divisão
6 – Dobro
7 – Quadrado
8 – Cubo
9 – Raiz Quadrada
0 – Sair"""

import math

def Operacoes(n, n1, n2):
	conta = 0
	if n == 1:
		n1 = float(input("Digite um numero: "))
		n2 = float(input("Digite outro numero: "))
		print('A soma entre os numeros digitados é: ')
		conta = n1 + n2
	elif n == 2:
		n1 = float(input("Digite um numero: "))
		n2 = float(input("Digite outro numero: "))
		print(f'A subtração entre os numeros digitados é: ')
		conta = n1 - n2
	elif n == 3:
		n1 = float(input("Digite um numero: "))
		n2 = float(input("Digite outro numero: "))
		print(f'"A divisão entre os numeros digitados é: ')
		conta = n1 / n2
	elif n == 4:
		n1 = float(input("Digite um numero: "))
		n2 = float(input("Digite outro numero: "))
		print(f'A multiplicação entre os numeros digitados é: ')
		conta = n1 * n2
	elif n == 5:
		n1 = float(input("Digite um numero: "))
		n2 = float(input("Digite outro numero: "))
		print(f'O resto da divisão entre os numeros digitados é: ')
		conta = n1 % n2
	elif n == 6:
		n1 = float(input("Digite um numero: "))
		n2 = 0
		print(f'O dobro do numero digitado é: ')
		conta = n1 * 2
	elif n == 7:
		n1 = float(input("Digite um numero: "))
		n2 = 0
		print(f'O numero digitado ao quadrado é: ')
		conta = n1 ** 2
	elif n == 8:
		n1 = float(input("Digite um numero: "))
		n2 = 0
		print(f"O numero digitado ao cubo é: ")
		conta = n1 ** 3
	elif n == 9:
		n1 = float(input("Digite um numero: "))
		n2 = 0
		print(f"A raiz quadrada do numero digitado é: ")
		conta = math.sqrt(n1)
	return conta


n1 = n2 = n3 = 0
n = int(input("1 - Soma\n2 - Subtração\n3 - Divisão\n4 - Multiplicação\n5 - Resto da divisão\n6 - Dobro\n7 - Quadrado\n8 - Cubo\n9 - Raiz quadrada\n0 - Sair\n\nEscolha qual operação deseja realizar ou digite 0 para sair: "))

if n == 1 or 2 or 3 or 4 or 5:
	print(Operacoes(n, n1, n2))
elif n == 0:
	print("Programa encerrado")
elif n == 6 or 7 or 8 or 9:
	print(Operacoes(n, n3, 0))