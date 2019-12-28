"""Elabore um programa que receba o nome e o ano de nascimento
de uma pessoa e mostre na tela a idade da pessoa."""

nome = str(input("Qual é o seu nome? "))
nasc = int(input("Em que ano você nasceu? "))
ano = int(input("Qual é o ano atual? "))
print(f'{nome} você tem {ano - nasc} anos')