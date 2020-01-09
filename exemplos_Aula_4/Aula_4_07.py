matriz = [
	[0, 0, 0],
	[0, 0, 0],
	[0, 0, 0]
]
print("Entre com o valor em cada posição da matriz: ")
for a in range(0, 3):
	for b in range(0, 3):
		matriz[a][b] = int(input(f"mat[{a}][{b}] = "))
print("\nExibindo os dados da matriz: ")
for a in range(0, 3):
	for b in range(0, 3):
		print(matriz[a][b])