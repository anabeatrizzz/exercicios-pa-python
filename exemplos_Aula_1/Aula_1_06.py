nome = input(str("Digite seu nome: "))
idade = input(str(f"{nome}, digite sua idade: "))
peso = input(str(f"{nome}, digite seu peso: "))

print("\n***Informações digitadas***")
print(f"{nome} tem {int(idade)} anos de idade e pesa {float(peso):.2f}")