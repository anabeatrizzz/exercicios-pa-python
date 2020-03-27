class Pessoa():
	def __init__(self, n=None, i=None, a=None, g=None):
		self.nome = n
		self.idade = i
		self.altura = a
		self.genero = g
	
	def retornaAtributos(self):
		print(f'Nome: {self.nome}\nIdade: {self.idade}\nAltura: {self.altura}\nGenero: {self.genero}')

	def calcularPesoIdeal(self):
		if self.genero in "Mm":
			print((72.7 * self.altura) - 58)
		else:
			print(f'{(62.1 * self.altura) - 44.7:.2f}')

class Aluno(Pessoa):
	# Init de Aluno com dois novos atributos e atributos de Pessoa
	def __init__(self, n=None, i=None, a=None, g=None, m=None, c=None):
		# Init de Pessoa para poder fazer a herança
		super().__init__(n=None, i=None, a=None, g=None)
		self.matricula = m
		self.curso = c

	def retornaAtributos(self):
		# usando super() para pegar um metodo da classe mae
		print(f'{super().retornaAtributos()}Matricula: {self.matricula}\nCurso: {self.curso}')

class Professor(Pessoa):
	def __init__(self, t=None, c=None):
		super().__init__(n=None, i=None, a=None, g=None)
		self.titulacao = t
		self.ch = c

	def retornaAtributos(self):
		print(f'{super().retornaAtributos()} Titulação: {self.titulacao}\nCH: {self.ch}')

a = Aluno()
a.nome = "Ana";
a.idade = 18;
a.altura = 1.70;
a.genero = "Feminino";
a.matricula = 1;
a.ch = "DS";
a.retornaAtributos();
