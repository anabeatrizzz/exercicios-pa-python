"""Escreva um programa que leia o nome e o preço de 10 produtos.
Logo após realizar o cadastro dos produtos, pedir para o usuário digitar
um valor, no qual deverá ser realizada uma pesquisa e exibir apenas
os produtos que possuem preço até o valor digitado pelo usuário."""

nomes = []
precos = []

for c in range(0, 10):
	nomes.append(str(input(f"Digite o nome do {c+1} produto")))
print()
for d in range(0, 10):
	precos.append(float(input(f"Digite o preco para o produto {nomes[d]}")))
print()
valor = float(input(f"Digite um valor: "))
for e in range(0, 10):
	if precos[e] <= valor:
		print(f"{nomes[e]} custa {precos[e]}")
