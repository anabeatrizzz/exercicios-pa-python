palavra = str(input("Digite uma palavra: "))
print(f"Vogais da palavra {palavra}")
vetor = []
for c in palavra:
	vetor.append(c)
tamanho = len(vetor)
for c in range(0, tamanho):
	if vetor[c] in "aAeEiIoOuU":
		print(vetor[c])