"""Escreva um programa que leia um vetor de 15 números inteiros
e exiba ao final apenas os números que estão armazenados
nas posições pares do vetor."""

numeros = []
for c in range(0, 15):
    numeros.append(int(input(f"Digite o {c+1} numero: ")))
for d in range(0, 15):
	if (d + 1) % 2 == 0:
		print(f"\n{numeros[d]}")
print("Estes sao os valores que estao nos indices pares")