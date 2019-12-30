"""Um comerciante deseja fazer o levantamento do lucro das mercadorias que ele comercializa.
Para isto, mandou digitar cada mercadoria com o nome, preço de compra preço
de venda das mercadorias.
Fazer um algoritmo que:
Determine e escreva quantas mercadorias proporcionam:
- Lucro menor 10%.
- Lucro entre 10% e 20%.
- Lucro maior que 20%.
- Determine e escreva o valor total de compra e de venda de todas as mercadorias, assim como o lucro total."""

totalc = totalv = lucrog = menorl = mediol = maiorl = 0
while True:
	nome = str(input("Produto: "))
	pcompra = float(input("Preço de compra: "))
	pvenda = float(input("Preço de venda: "))
	x = str(input("Deseja cadastrar outro produto? ")).lower()
	print("---------- xxx ----------")
	
	lucro = pvenda - pcompra
	totalc += pcompra
	totalv += pvenda
	lucrog += lucro

	if x in "Nn" or x == "nao":
		break
	
	if lucro < (pcompra * 0.1):
		menorl += 1
	elif lucro >= (pcompra * 0.1) and lucro <= (pcompra * 0.2):
		mediol += 1
	elif lucro > (pcompra * 0.2):
		maiorl += 1
print(f"Produtos com 10% de lucro: {menorl}\nProdutos entre 10% e 20% de lucro: {mediol}\nProdutos com mais de 20% de lucro: {maiorl}\nO valor total de compra é: {totalc}\nO valor total de venda é: {totalv}\nO lucro geral é: {lucrog}")