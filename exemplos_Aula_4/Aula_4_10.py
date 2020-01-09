def exibir(m):
	for a in range(0, 5):
		for b in range(0, 3):
			print(m[a][b])

nomes = [
	[0, 0, 0],
	[0, 0, 0],
	[0, 0, 0],
	[0, 0, 0],
	[0, 0, 0],
]

n = "Fulano"
cont = 0
for a in range(0, 5):
	for b in range(0, 3):
		cont += 1
		nomes[a][b] = f"{n} {cont}"
print("*** Nomes cadastrados na matriz ***")
exibir(nomes)