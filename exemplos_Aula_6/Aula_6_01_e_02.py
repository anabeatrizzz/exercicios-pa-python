class Pessoa():
	def __init__(self, n=None):
		self.nome = n

	def str(self):
		print(self.nome)

p = Pessoa()
p.nome = "Ana"
p.str()
