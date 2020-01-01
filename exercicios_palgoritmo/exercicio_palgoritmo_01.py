"""Elaborar um algoritmo em que efetue a leitura do nome e do genero de uma pessoa,
apresentando como saída uma das seguintes mensagens: "Ilmo Sr.", para o genero informado como masculino,
ou a mensagem "Ilma Sra.", para o genero informado como feminino.
Apresente na sequência da mensagem impressa o nome da pessoa."""

nome = str(input("Qual é seu nome? "))
g = str(input("Qual é seu genero? ")).lower()
if g in "Ff" or g == "feminino":
	print(f'Ilma Sra. {nome}')
if g in "Mm" or g == "masculino":
	print(f'Ilmo Sr. {nome}')
