import time
import os
cont2 = 0

class Carros():
	def __init__(self):
		self.modelo = []
		self.ano = []
		self.cor = []
		self.marca = []

def Enfeitar(numero):
	if numero == 5:
		print()
		print("Espere 5 segundos, o sistema está carregando...")
		time.sleep(5)
		clear = lambda: os.system('clear')
		clear()
	if numero == 3:
		print()
		print("Espere 3 segundos, o sistema está carregando...")
		time.sleep(3)
		clear = lambda: os.system('clear')
		clear()

def opcao1(carro):
	carro.modelo.append(str(input("Digite o MODELO do carro: ")))
	carro.ano.append(str(input("Digite o ANO do carro: ")))
	carro.cor.append(str(input("Digite a COR do carro: ")))
	carro.marca.append(str(input("Digite a MARCA do carro: ")))

def opcao2(carro):
	opcao_ano = str(input("Digite um ano: "))
	print("\033[32mOs carros cadastrados neste ano são:\033[m")
	for x in range(0, cont2):
		if carro.ano[x] == opcao_ano:
			print(carro.modelo[x])
	Enfeitar(5)

def opcao3(carro):
	opcao_modelo = str(input("Digite um modelo: "))
	for x in range(0, cont2):
		if carro.modelo[x] == opcao_modelo:
			print(f"\033[32mO modelo mencionado é da marca:\033[m {carro.marca[x]}")
	Enfeitar(5)

def opcao4(carro):
	opcao_cor = str(input("Digite uma cor: "))
	print(f"\033[32mOs carros que têm essa cor são:\033[m")
	for x in range(0, cont2):
		if carro.cor[x] == opcao_cor:
			print(carro.modelo[x])
	Enfeitar(5)

def opcao5(carro):
	print("\033[32mTodos os carros cadastrados são:\033[m")
	for x in range(0, cont2):
		print(carro.modelo[x])
	Enfeitar(5)

def opcao6(carro):
	opcao_modelo2 = str(input("Digite um modelo de carro: "))
	opcao_categoria = int(input("1 - Nome do modelo\n2 - Ano do modelo\n3 - Cor do modelo\n4 - Marca do modelo\nQual categoria deseja alterar? "))
	valor_novo = str(input("Digite o valor novo: "))
	for x in range(0, cont2):
		if carro.modelo[x] == opcao_modelo2:
			if opcao_categoria == 1:
				carro.modelo[x] = valor_novo
			elif opcao_categoria == 2:
				carro.ano[x] = valor_novo
			elif opcao_categoria == 3:
				carro.cor[x] = valor_novo
			elif opcao_categoria == 4:
				carro.marca[x] = valor_novo
	print("\033[32mValor alterado com sucesso!\033[m")
	Enfeitar(3)

def opcao7(carro):
	opcao_modelo3 = str(input("Digite o modelo de carro que deseja excluir: "))
	for x in range(0, cont2):
		if carro.modelo[x] == opcao_modelo3:
			carro.modelo[x] = "\033[31mMODELO EXCLUIDO\033[m"
			carro.ano[x] = "\033[31mANO EXCLUIDO\033[m"
			carro.cor[x] = "\033[31mCOR EXCLUIDA\033[m"
			carro.marca[x] = "\033[31mMARCA EXCLUIDA\033[m"
	print("\033[32mCarro excluido com sucesso!\033[m")
	Enfeitar(3)


carro = Carros()
while True:
	print("1 - Cadastrar carro\n2 - Consultar carro por ano de fabricação\n3 - Consultar carro por modelo\n4 - Consultar carro por cor\n5 - Exibir todos os carros cadastrados\n6 - Alterar algum dado de um carro\n7 - Excluir um carro\n0 - Sair")
	print()
	opcao = int(input("Digite a sua opção: "))
	if opcao == 1:
		cont2 += 1
		opcao1(carro)
		print("\033[32mCarro cadastrado com sucesso!\033[m")
		Enfeitar(3)
	elif opcao == 0:
		break
	if (opcao == 2 or opcao == 3 or opcao == 4 or opcao == 5 or opcao == 6 or opcao == 7) and cont2 == 0:
		print("Não foi possivel executar o pedido pois, não há nenhum carro cadastrado")
		break
	elif opcao == 2 and cont2 > 0:
		opcao2(carro)
	elif opcao == 3 and cont2 > 0:
		opcao3(carro)
	elif opcao == 4 and cont2 > 0:
		opcao4(carro)
	elif opcao == 5 and cont2 > 0:
		opcao5(carro)
	elif opcao == 6 and cont2 > 0:
		opcao6(carro)
	elif opcao == 7 and cont2 > 0:
		opcao7(carro)