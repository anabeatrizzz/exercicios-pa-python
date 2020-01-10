class Livros():
	def __init__(self):
		self.titulo = ""
		self.ano = 0
		self.preco = 0.0

def exibir(l):
	print("Exibindo os dados do livro...")
	print(f"Titulo do livro: {l.titulo}")
	print(f"Ano de lançamento: {l.ano}")
	print(f"Preço: R${l.preco}")

def cadastrar():
	livro = Livros()
	print("Cadastrando um livro...")
	livro.titulo = str(input("Titulo do livro: "))
	livro.ano = int(input("Ano de lançamento: "))
	livro.preco = float(input("Preço: "))
	return livro

livro = Livros()
livro = cadastrar()
print()
exibir(livro)