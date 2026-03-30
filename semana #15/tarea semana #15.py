productos = {}

while True:
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio: "))
    
    productos[nombre] = precio
    
    opcion = input("¿Desea agregar otro producto? (si/no): ")
    if opcion.lower() != "si":
        break

print("\nLista de productos:")
for producto, precio in productos.items():
    print(producto, "-> $", precio)
