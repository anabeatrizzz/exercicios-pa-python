nome1 = str(input("Digite o nome da primeira pessoa: "))
idade1 = int(input("Digite a idade da primeira pessoa: "))

nome2 = str(input("Digite o nome da segunda pessoa: "))
idade2 = int(input("Digite a idade da segunda pessoa: "))

if idade1 > idade2:
	print(f"{nome1} é mais velho(a) e tem {idade1} anos de idade")
elif idade2 > idade1:
	print(f"{nome2} é mais velho(a) e tem {idade2} anos de idade")
else:
	print(f"{nome1} e {nome2} tem {idade1} anos de idade")