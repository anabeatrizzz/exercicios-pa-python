while True:
	opcao = int(input("1 - Par ou impar\n2 - Decrescente até 0\n3 - Sair\n\nInforme a opção desejada: "))
	if opcao == 1:
		n = int(input("Digite um numero: "))
		IP = "par" if n % 2 == 0 else "impar"
		print(f"{n} é {IP}\n")
	elif opcao == 2:
		n = int(input("Digite um numero: "))
		while n >= 0:
			print(n)
			n -= 1
		print()
	elif opcao == 3:
		print("Programa encerrado")
		break
	else:
		print("Opção invalida, tente novamente")