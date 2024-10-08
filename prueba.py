# main.py

# Función para mostrar el menú de productos
def mostrar_menu():
    print("Productos disponibles:")
    for index, producto in enumerate(productos):
        print(f"{index + 1}. {producto['nombre']} - ${producto['precio']} (Disponible: {producto['cantidad']})")

# Función para agregar productos al carrito
def agregar_carrito():
    while True:
        mostrar_menu()
        seleccion = input("Selecciona el número del producto que deseas agregar (o 'fin' para terminar): ")
        if seleccion.lower() == 'fin':
            break
        try:
            seleccion = int(seleccion) - 1
            if 0 <= seleccion < len(productos):
                cantidad = int(input(f"Ingrese la cantidad de {productos[seleccion]['nombre']} que desea agregar: "))
                if cantidad <= productos[seleccion]['cantidad']:
                    carrito.append({'producto': productos[seleccion], 'cantidad': cantidad})
                    productos[seleccion]['cantidad'] -= cantidad
                    print(f"Agregado {cantidad} de {productos[seleccion]['nombre']} al carrito.")
                else:
                    print("No hay suficiente stock.")
            else:
                print("Selección no válida.")
        except ValueError:
            print("Por favor, ingresa un número válido.")

# Función para calcular el total de la compra
def calcular_total():
    total = sum(item['producto']['precio'] * item['cantidad'] for item in carrito)
    if total > 100:  # Aplicar un descuento si el total es mayor a 100
        total *= 0.9  # Descuento del 10%
    return total

# Función para finalizar la compra
def finalizar_compra(nombre_cliente):
    total = calcular_total()
    print(f"\nResumen de compra de {nombre_cliente}:")
    for item in carrito:
        print(f"{item['cantidad']} x {item['producto']['nombre']} - ${item['producto']['precio']} cada uno")
    print(f"Total a pagar: ${total:.2f}")
    # Guardar reporte en archivo
    with open("reporte.txt", "a") as file:
        file.write(f"{nombre_cliente} compró:\n")
        for item in carrito:
            file.write(f"{item['cantidad']} x {item['producto']['nombre']} - ${item['producto']['precio']} cada uno\n")
        file.write(f"Total a pagar: ${total:.2f}\n\n")

# Lista de productos
productos = [
    {'nombre': 'Producto A', 'precio': 30.00, 'cantidad': 10},
    {'nombre': 'Producto B', 'precio': 20.00, 'cantidad': 5},
    {'nombre': 'Producto C', 'precio': 50.00, 'cantidad': 2}
]

carrito = []

# Programa principal
if __name__ == "__main__":
    nombre_cliente = input("Ingresa tu nombre: ")
    agregar_carrito()
    finalizar_compra(nombre_cliente)
