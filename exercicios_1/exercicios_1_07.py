# Escreva um programa que leia o nome de duas pessoas e ao final exiba:
# O nome das duas pessoas com todos os caracteres maiúsculos
# A quantidade de caracteres de cada nome
# Apenas os três primeiros caracteres de cada nome

nome1 = str(input("Escreva um nome: "))
nome2 = str(input("Escreva outro nome: "))

print(f"\nO primeiro nome em maiusculo: {nome1.upper()}")
print(f"O segundo nome em maiusculo: {nome2.upper()}")

print(f"Seu primeiro nome tem {len(nome1)} letras")
print(f"Seu segundo nome tem {len(nome2)} letras")

print(f"As primeiras tres letras do seu primeiro nome são: {nome1[0:3]}")
print(f"As primeiras tres letras do seu segundo nome são: {nome2[0:3]}")