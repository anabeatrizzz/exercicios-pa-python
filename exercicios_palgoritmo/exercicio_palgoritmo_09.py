"""Elaborar um algoritmo que efetue a leitura de um valor que esteja entre a faixa de 1 a 9.
Após a leitura do valor fornecido pelo usuário, o programa deverá indicar uma de duas mensagens: “O valor está na faixa permitida”, caso o usuário forneça o valor nesta faixa, ou a mensagem “O valor está fora da faixa permitida”, caso o usuário forneça valores menores que 1 ou maiores que 9."""

num = int(input("Digite um numero: "))
if num >= 1 and num <= 9:
	print(f"O valor {num} está na faixa permitida")
elif num < 1 or num > 9:
	print(f"O valor {num} está fora da faixa permitida")