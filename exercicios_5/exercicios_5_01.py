class Data():
	def __init__(self):
		self.dia = 0
		self.mes = 0
		self.ano = 0

def VerificaDia(dia, mes, resultado):
	if (mes == 1 or 3 or 5 or 7 or 8 or 10 or 12) and dia > 31 or dia <= 0:
		print("\033[31mData invalida, informe um dia menor que 31 e não negativo.\033[m")
		resultado = False
	elif (mes == 4 or 6 or 9 or 11) and dia > 30 or dia <= 0:
		print("\033[31mData invalida, informe um dia menor igual a 30 e não negativo.\033[m")
		resultado = False
	else:
		resultado = True
	return resultado

def VerificaBissexto(ano, mes, dia, resultado):
	if (ano % 4 == 0) and (ano % 100 != 0) or (ano % 400 == 0) and (mes == 2) and (dia > 29):
		print("\033[31mData invalida, fevereiro apenas possui 29 dias neste ano.\033[m")
		resultado = False
	elif (ano % 4 != 0) and (mes == 2) and (dia > 28):
		print("\033[31mData invalida, fevereiro neste ano apenas possui 28 dias.\033[m")
		resultado = False
	else:
		resultado = True
	return resultado

def VerificaFevereiro(dia, mes, resultado):
	if dia > 29 and mes == 2:
		print("\033[31mData invalida, fevereiro apenas pode possuir 29 dias.\033[m")
		resultado = False
	else:
		resultado = True
	return resultado

def VerificaMes(mes, resultado):
	if 12 > mes <= 0:
		print("\033[31mData invalida, digite um mes válido.\033[m")
		resultado = False
	else:
		resultado = True
	return resultado

def VerificaAno(ano, resultado):
	if len(str(ano)) > 4 or len(str(ano)) < 4:
		print("\033[31mData invalida, digite um ano com 4 digitos.\033[m")
		resultado = False
	else:
		resultado = True
	return resultado

def VerificaTudo(dia, mes, ano, resultado):
	if VerificaDia(dia, mes, resultado) and VerificaMes(mes, resultado) and VerificaFevereiro(dia, mes, resultado) and VerificaBissexto(ano, mes, dia, resultado) and VerificaAno(ano, resultado):
		print(f"\033[32mA data digitada foi {dia}/{mes}/{ano} e é uma data valida!\033[m")

resultado = False

data = Data()
data.dia = int(input("Digite um dia: "))
data.mes = int(input("Digite um mês: "))
data.ano = int(input("Digite um ano: "))

VerificaDia(data.dia, data.mes, resultado)
VerificaMes(data.mes, resultado)
VerificaFevereiro(data.dia, data.mes, resultado)
VerificaBissexto(data.ano, data.mes, data.dia, resultado)
VerificaAno(data.ano, resultado)
VerificaTudo(data.dia, data.mes, data.ano, resultado)