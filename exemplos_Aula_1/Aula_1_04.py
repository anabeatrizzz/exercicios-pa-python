nome = "Tiago"
sobrenome = "Souza"
completo = nome + " " + sobrenome

print(f"1) {nome} {sobrenome}")
print(f"2) {completo}")
print(f"3) {nome} possui {len(nome)} caracteres")
print(f"4) {sobrenome} possui {len(sobrenome)} caracteres")
print(f"5) {completo} possui {len(completo)} caracteres - incluindo espaços em branco")
print(f"6) {nome} em minusculo {nome.lower()}")
print(f"7) {nome} em maisculo {nome.upper()}")
print(f"8) {nome} é igual a {sobrenome} = {nome == sobrenome}")
print(f"9) {nome} substring iniciando na posição 2 e pegando 2 caracteres - {nome[2:4]}")