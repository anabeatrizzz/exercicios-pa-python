class Pessoa():
	def __init__(self, n, i, a, g):
		self.nome = n
		self.idade = i
		self.altura = a
		self.genero = g

	def Pessoa(self):
		self.nome = None
		self.idade = None
		self.altura = None
		self.genero = None

	def retornaAtributos(self):
		print(f'Nome: {self.nome}\nIdade: {self.idade}\nAltura: {self.altura}\nGenero: {self.genero}')

	def calcularPesoIdeal(self):
		if self.genero in "Mm":
			print((72.7 * self.altura) - 58)
		else:
			print(f'{(62.1 * self.altura) - 44.7:.2f}')

nome = str(input("Nome da pessoa: "))
idade = int(input(f'Idade de {nome}: '))
altura = float(input(f'Altura de {nome}: '))
genero = str(input(f'Genero de {nome}: '))
print()
p = Pessoa(nome, idade, altura, genero)

print('Exibindo dados:')
p.retornaAtributos()

print()
print('Peso ideal:')
p.calcularPesoIdeal()
