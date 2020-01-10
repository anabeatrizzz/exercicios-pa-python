class Dados():
	def __init__(self):
		self.dia = 0
		self.mes = 0
		self.ano = 0

nasc = Dados()
nasc.dia = int(input("Digite o dia de seu nascimento: "))
nasc.mes = int(input("Digite o mes de seu nascimento: "))
nasc.ano = int(input("Digite o ano de seu nascimento: "))
print(f"Data de nascimento informada: {nasc.dia}/{nasc.mes}/{nasc.ano}")