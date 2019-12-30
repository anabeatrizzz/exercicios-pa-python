"""Fazer um algoritmo para ler o ano de nascimento de uma pessoa, calcular e mostrar sua idade e, também, verificar e mostrar se ela já tem idade para votar (16 anos ou mais) e para conseguir a Carteira de Habilitação (18 anos ou mais)."""

from datetime import date

num = int(input("Em que ano você nasceu? "))
idade = date.today().year - num
if idade >= 16:
	print(f"Você tem {idade} anos\nE por isso já pode votar.")
if idade >= 18:
	print(f"Você tem {idade} anos\nE por isso você já pode ter uma CNH.")
else:
	print("Você não tem idade para votar nem para ter uma CNH")