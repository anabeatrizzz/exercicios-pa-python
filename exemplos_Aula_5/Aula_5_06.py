class Livros():
	def __init__(self):
		self.titulo = []
		self.ano = []
		self.preco = []

def cadastrar():
	livro = Livros()
	print("Cadastrando um livro...")
	for c in range(0, 3):
		livro.titulo.append(str(input("Titulo do livro: ")))
		livro.ano.append(int(input("Ano de lançamento: ")))
		livro.preco.append(float(input("Preço: ")))
		print()
	return livro

def exibir(l):
	print("Exibindo os dados do livro...")
	for c in range(0, 3):
		print(f"Titulo do livro: {l.titulo[c]}")
		print(f"Ano de lançamento: {l.ano[c]}")
		print(f"Preço: R${l.preco[c]}")
		print()

livro = Livros()
livro = cadastrar()
exibir(livro)