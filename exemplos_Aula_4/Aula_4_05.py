def exibirDados(t):
	for c in range(0, len(t)):
		print(f"{c+1}o time: {t[c]}")


tam = 10
times = []
print("*** Times de Futebol ***")
for c in range(0, tam):
	times.append(str(input(f"Nome do {c+1}o time: ")))
print("\n*** Times cadastrados no vetor ***")
exibirDados(times)