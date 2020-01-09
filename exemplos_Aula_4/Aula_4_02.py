nomes = []
for c in range(0, 10):
	nomes.append(str(input(f"Digite o {c+1}o nome: ")))
for c in range(0, 10):
	print(f"{c+1}o nome: {nomes[c]}")