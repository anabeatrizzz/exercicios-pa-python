"""Escreva um programa que armazene os números de 1 a 25 em uma matriz 5x5
e ao final exiba apenas os valores das diagonais desta matriz."""

matriz = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]
print(f"{matriz[0][0]}             {matriz[0][4]}")
print(f"   {matriz[1][1]}      {matriz[1][3]}")
print(f"      {matriz[2][2]}")
print(f"   {matriz[3][1]}     {matriz[3][3]}")
print(f"{matriz[4][0]}            {matriz[4][4]}")