opcao = str(input("Inclusão\nAlteração\nExclusão\nEscolha sua opção: ")).lower()

if opcao == "inclusão":
	print("Você escolheu a opção inclusão.")
elif opcao == "alteração":
	print("Você escolheu a opção alteração.")
elif opcao == "exclusão":
	print("Você escolheu a opção exclusão.")
else:
	print("Você escolheu uma opção invalida.")