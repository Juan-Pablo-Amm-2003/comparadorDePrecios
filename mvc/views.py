from mvc.controllers import inicializar_archivos, ProductosController

# Llamar a la función para verificar y crear archivos
inicializar_archivos()

# Función para mostrar el menú y manejar las opciones del usuario
def menu():
    print("\nBienvenido al sistema de gestión de productos:")
    print("1. Comparar precios de un producto")
    print("2. Agregar un nuevo producto")
    print("3. Modificar el precio de un producto")
    print("4. Salir")

    opcion = input("Ingrese el número de la opción que desea ejecutar: ")
    return opcion

def main():
    controller = ProductosController()

    print("Bienvenido al sistema de gestión de productos:")
    print("1. Comparar precios de un producto")
    print("2. Agregar un nuevo producto")
    print("3. Modificar el precio de un producto")
    print("4. Salir")

    while True:
        opcion = input("Ingrese el número de la opción que desea ejecutar: ")

        if opcion == '1':
            producto = input("Ingrese el nombre del producto a comparar: ")
            precios = controller.comparar_precios_producto(producto)
            if precios:
                if all(precios.values()):
                    print(f"Precios de {producto}: Lista 1 ${precios['lista1']}, Lista 2 ${precios['lista2']}, Lista 3 ${precios['lista3']}")
                else:
                    print(f"El producto {producto} no existe en alguna de las listas.")
            else:
                print(f"El producto {producto} no existe en ninguna lista.")

        elif opcion == '2':
            producto = input("Ingrese el nombre del producto a agregar: ")
            precios = solicitar_precio_producto()
            controller.agregar_producto(producto, precios)

        elif opcion == '3':
            producto = input("Ingrese el nombre del producto a modificar: ")
            nuevo_precio = input("Ingrese el nuevo precio del producto: ")
            controller.modificar_precio(producto, nuevo_precio)

        elif opcion == '4':
            print("Saliendo del programa...")
            break

        else:
            print("Opción inválida. Por favor, ingrese un número del 1 al 4.")


if __name__ == "__main__":
    main()

def solicitar_precio_producto():
    precios = {}
    for proveedor in ["lista1", "lista2", "lista3"]:
        precio = input(f"Ingrese el precio para {proveedor}: $")
        try:
            precios[proveedor] = float(precio.replace('$', '').strip())
        except ValueError:
            print(f"El precio ingresado para {proveedor} no es válido. Ingrese un número válido.")
    return precios

def mostrar_precios(precios):
    for proveedor, precio in precios.items():
        print(f"{proveedor}: ${precio}")
