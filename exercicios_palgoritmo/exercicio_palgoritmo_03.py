"""Tendo como dados de entrada a altura e o sexo de uma pessoa, construa um algoritmo que calcule peso ideal, utilizando as seguintes fórmulas:
Para homens: (72.7 * h) - 58
Para mulheres: (62.1*h) – 44.7 Onde h equivale a altura da pessoa."""

h = float(input("Digite a sua altura: "))
g = str(input("Digite o seu genero: ")).lower()
if g in "Mm" or g == "masculino":
	print(f"O peso ideal para você é {(72.7 * h) - 58:.0f}kg")
if g in "Ff" or g == "feminino":
	print(f"O peso ideal para você é {(62.1 * h) - 44.7:.0f}kg")