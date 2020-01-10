import os

class Aluno():
	def __init__(self):
		self.nome = []
		self.matricula = []
		self.nota = []

alunos = Aluno()
print("CADASTRANDO DADOS")
for c in range(0, 5):
	alunos.nome.append(str(input(f"Nome do(a) {c+1}o(a) aluno(a): ")))
	alunos.matricula.append(int(input("Matricula: ")))
	alunos.nota.append(float(input("Nota: ")))
clear = lambda: os.system('clear')
clear()
print("EXIBINDO DADOS")
for c in range(0, 5):
	print(f"Nome do(a) {c+1}o(a) aluno(a): {alunos.nome[c]}")
	print(f"Matricula: {alunos.matricula[c]}")
	print(f"Nota: {alunos.nota[c]}")