class Pessoa():
	def __init(self):
		self.nome = ""
		self.idade = 0
		self.altura = 0.0

pessoa1 = Pessoa()
pessoa2 = Pessoa()
pessoa1.nome = "Ana"
pessoa2.nome = "Beatriz";

pessoa1.idade = 18;
pessoa2.idade = 17;

pessoa1.altura = 1.70;
pessoa2.altura = 1.60;

print(f"{pessoa1.nome}, com {pessoa1.idade} anos, mede {pessoa1.altura}m de altura.")
print(f"{pessoa2.nome}, com {pessoa2.idade} anos, mede {pessoa2.altura}m de altura.")