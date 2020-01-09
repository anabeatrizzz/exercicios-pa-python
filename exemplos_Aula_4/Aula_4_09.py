matriz = [
	[1, 42, 23, 14, 51],
	[22, 32, 55, 54, 12]
]
print("Os elementos pares da matriz são: ")
for a in range(0, 2):
	for b in range(0, 5):
		if matriz[a][b] % 2 == 0:
			print(matriz[a][b])