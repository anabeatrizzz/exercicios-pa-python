verdade = "sim"
falso = "não"

a = int(input("Digite um numero inteiro: "))
b = int(input("Digite outro numero inteiro: "))

print(f"{a} > {b}? Resposta: {verdade if a > b else falso}")