soma = 0
while True:
	n = float(input("Digite um numero (digite 0 para sair): "))
	if n == 0:
		break
	soma += n
	print(f"\nAcumulo da soma = {soma}")
	print("----------")