"""Escreva um programa que leia o nome de 10 alunos (vetor).
Para cada aluno devem ser registradas 3 notas (matriz).
Calcular a média das notas de cada aluno e armazenar em um vetor.
Ao final deverá ser exibido na tela um relatório com os dados de todos os alunos (nome, notas, média)
e também a informação se o aluno foi aprovado ou reprovado (média para aprovação 7,0).
Para o caso de aprovado exibir todos os dados do aluno na cor azul, caso contrário exibir os dados na cor vermelha"""

ficha = []
for c in range(0, 10):
	nome = str(input('Nome: '))
	nota1 = float(input('Primeira nota: '))
	nota2 = float(input('Segunda nota: '))
	nota3 = float(input('Terceira nota: '))
	print()
	media = (nota1 + nota2 + nota3) / 3
	ficha.append([nome, [nota1, nota2, nota3], media])
print(f'ALUNOS\t|\t\tNOTAS\t\t|\t\tMEDIA')
for i, a in enumerate(ficha):
	if a[2] >= 7:
		print(f'\033[36m{a[0]}\t\t\t{ficha[i][1][0]}\t{ficha[i][1][1]}\t{ficha[i][1][2]}\t\t\t\t{a[2]:.2f}\033[m')
	else:
		print(f'\033[31m{a[0]}\t\t\t{ficha[i][1][0]}\t{ficha[i][1][1]}\t{ficha[i][1][2]}\t\t\t\t{a[2]:.2f}\033[m')
