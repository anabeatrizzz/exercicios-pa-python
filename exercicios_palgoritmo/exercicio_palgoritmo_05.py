"""Escrever um algoritmo para ler três valores inteiros e escrever na tela o maior e o menor deles.
Considere que todos os valores são diferentes."""

pri = int(input("Digite o primeiro valor: "))
seg = int(input("Digite o segundo valor: "))
ter = int(input("Digite o terceiro valor: "))

if seg < pri > ter:
	print("O primeiro numero digitado é o maior de todos.")
elif pri < seg > ter:
	print("O segundo numero digitado é o maior de todos.")
elif pri < ter > seg:
	print("O terceiro numero digitado é o maior de todos.")
