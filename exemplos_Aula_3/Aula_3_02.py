def Digite():
	print("Digite uma palavra: ")

def Tamanho(p):
	return len(p)

Digite()
p = str(input())
t = Tamanho(p)
print(f"{p} possui {t} caracteres")