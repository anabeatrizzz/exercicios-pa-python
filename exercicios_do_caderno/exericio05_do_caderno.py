"""Elabore um programa que mostre na tela se uma pessoa é maior ou menor de idade."""

nome = str(input("Qual é o seu nome? "))
idade = int(input("Qual é a sua idade? "))
if idade >= 18:
    print(f'{nome}, você é maior de idade.')
else:
    print(f'{nome}, você é menor de idade.')