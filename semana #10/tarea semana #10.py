# Parte 1: Programa con matriz
# Declarar una matriz de 3x3 con números enteros

matriz = [
    [2, 4, 6],
    [1, 3, 5],
    [7, 8, 9]
]

print("Valores de la matriz 3x3:")
print()

# Recorrer la matriz con ciclos anidados
for i in range(3):
    for j in range(3):
        print(matriz[i][j], end=" ")
    print()  # Salto de línea después de cada fila

