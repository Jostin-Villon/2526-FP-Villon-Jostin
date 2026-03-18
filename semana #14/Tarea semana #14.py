def calcular_promedio(nota1, nota2, nota3):
    promedio = (nota1 + nota2 + nota3) / 3
    return promedio

n1 = float(input("Ingrese la primera nota: "))
n2 = float(input("Ingrese la segunda nota: "))
n3 = float(input("Ingrese la tercera nota: "))

resultado = calcular_promedio(n1, n2, n3)

print("El promedio es:", round(resultado, 2))