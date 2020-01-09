salario_min = 678.00
salarios = []
for c in range(0, 10):
	salarios.append((c + c) * salario_min)
for c in range(0, 10):
	print(f"{c+1} salarios(s) minimo(s) = {salarios[c]}")