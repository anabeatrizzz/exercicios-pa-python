def cadastro():
	auxiliar = []
	for c in range(0, 5):
		auxiliar.append(str(input(f"Digite o nome do {c+1}o curso: ")))
	return auxiliar

tam = 5
cursos = []
print("*** Cursos tecnicos ***")
cursos = cadastro()
print("*** Cursos cadastrados no vetor ***")
for c in range(0, 5):
	print(f"{c+1}o curso: {cursos[c]}")