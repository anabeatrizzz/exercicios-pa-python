def PessoaMaisVelha(n1, i1, n2, i2):
	if i1 > i2:
		return f"{n1} é a pessoa mais velha"
	else:
		if i2 > i1:
			return f"{n2} é a pessoa mais velha"
		else:
			return f"{n1} e {n2} tem a mesma idade"

nome1 = str(input("Digite o nome da primeira pessoa: "))
idade1 = int(input("Digite a idade da primeira pessoa: "))

nome2 = str(input("Digite o nome da segunda pessoa: "))
idade2 = int(input("Digite a idade da segunda pessoa: "))

texto = PessoaMaisVelha(nome1, idade1, nome2, idade2)

print(texto)