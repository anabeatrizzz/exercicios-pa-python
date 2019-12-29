class Alunos():
	def __init__(self):
		self.nome = []
		self.nota1 = []
		self.nota2 = []
		self.media = []
		self.situacao = []

def Tabela(matriz):
	print("|\tNOME\t|\t1a NOTA\t|\t2a NOTA\t|\tMÉDIA\t|\tSITUAÇÃO\t|")
	for x in range(0, 15):
		if matriz.media[x] >= 7:
			matriz.situacao.append("Aprovado(a)")
			print(f"\033[34m|\t{matriz.nome[x]}\t|\t{matriz.nota1[x]}\t|\t{matriz.nota2[x]}\t|\t{matriz.media[x]}\t|\t{matriz.situacao[x]}\t|\033[m")
		else:
			matriz.situacao.append("Reprovado(a)")
			print(f"\033[31m|\t{matriz.nome[x]}\t|\t{matriz.nota1[x]}\t|\t{matriz.nota2[x]}\t|\t{matriz.media[x]}\t|\t{matriz.situacao[x]}\t|\033[m")

aluno = Alunos()
for c in range(0, 15):
	aluno.nome.append(str(input(f"Nome do(a) {c+1}o(a) aluno(a): ")))
for x in range(0, 15):
	print()
	print(f"Informe duas notas para o(a) aluno(a) {aluno.nome[x]}")
	aluno.nota1.append(float(input("1a nota: ")))
	aluno.nota2.append(float(input("2a nota: ")))
for a in range(0, 15):
	aluno.media.append((aluno.nota1[a] + aluno.nota2[a]) / 2)
print()
Tabela(aluno)