from mvc.views import menu
from mvc.controllers import ProductosController

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
            if all(precios.values()):
                print(f"Precios de {producto}: Lista 1 ${precios['lista1']}, Lista 2 ${precios['lista2']}, Lista 3 ${precios['lista3']}")
            else:
                print(f"El producto {producto} no está disponible en alguna de las listas.")

        elif opcion == '2':
            producto = input("Ingrese el nombre del producto a agregar: ")
            precios = solicitar_precio_producto()
            controller.agregar_producto(producto, precios)

        elif opcion == '3':
            producto = input("Ingrese el nombre del producto a modificar: ")
            nuevo_precio = solicitar_nuevo_precio()

            proveedor = input("Ingrese el proveedor específico (lista1, lista2, lista3) o presione Enter para modificar en todos: ").strip().lower()

            if proveedor and proveedor in controller.lista_productos:
                controller.modificar_precio(producto, nuevo_precio, proveedor)
            elif not proveedor:
                controller.modificar_precio(producto, nuevo_precio)
            else:
                print(f"El proveedor {proveedor} no existe. No se realizó ninguna modificación.")

        elif opcion == '4':
            print("Saliendo del programa...")
            break

        else:
            print("Opción inválida. Por favor, ingrese un número del 1 al 4.")

def solicitar_precio_producto():
    precios = {}
    for proveedor in ["lista1", "lista2", "lista3"]:
        while True:
            precio = input(f"Ingrese el precio para {proveedor}: $")
            try:
                precios[proveedor] = float(precio.replace('$', '').strip())
                break
            except ValueError:
                print(f"El precio ingresado para {proveedor} no es válido. Ingrese un número válido.")
    return precios

def solicitar_nuevo_precio():
    while True:
        nuevo_precio = input("Ingrese el nuevo precio: $")
        try:
            return float(nuevo_precio.replace('$', '').strip())
        except ValueError:
            print("El precio ingresado no es válido. Ingrese un número válido.")

if __name__ == "__main__":
    main()
