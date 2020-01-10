import os

class Livros():
	def __init__(self):
		self.titulo = [[0, 0],[0, 0],[0, 0]]
		self.ano = [[0, 0],[0, 0],[0, 0]]
		self.preco = [[0, 0],[0, 0],[0, 0]]

def cadastrar():
	livro = Livros()
	print("Cadastrando um livro...")
	for c in range(0, 3):
		for d in range(0, 2):
			livro.titulo[c][d]= str(input("Titulo do livro: "))
			livro.ano[c][d]= int(input("Ano de lançamento: "))
			livro.preco[c][d] = float(input("Preço: "))
			print()
	return livro

def exibir(l):
	for c in range(0, 3):
		for d in range(0, 2):
			print(f"Titulo: {l.titulo[c][d]}")
			print(f"Ano: {l.ano[c][d]}")
			print(f"Preço: {l.preco[c][d]}")
			print()

livro = Livros()
livro = cadastrar()
clear = lambda: os.system('clear')
clear()
exibir(livro)