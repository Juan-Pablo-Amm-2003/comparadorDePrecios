# mvc/controllers.py

from mvc.models import ListaProductos

def inicializar_archivos():
    # Aquí podrías implementar lógica adicional si es necesario
    pass

class ProductosController:
    def __init__(self):
        self.lista_productos = {
            "lista1": ListaProductos("productos_lista1.txt"),
            "lista2": ListaProductos("productos_lista2.txt"),
            "lista3": ListaProductos("productos_lista3.txt")
        }

    def comparar_precios_producto(self, producto):
        precios = {}
        for key, lista in self.lista_productos.items():
            precio = lista.comparar_producto(producto)
            precios[key] = precio
        return precios

    def agregar_producto(self, producto, precios):
        for key, lista in self.lista_productos.items():
            lista.agregar_producto(producto, precios[key])

    def modificar_precio(self, producto, nuevo_precio, proveedor=None):
        if proveedor is None:
            proveedores = self.lista_productos.keys()
        else:
            proveedores = [proveedor]

        for key in proveedores:
            lista = self.lista_productos[key]
            if producto in lista.productos:
                lista.modificar_precio(producto, nuevo_precio)

    def mostrar_productos(self):
        for key, lista in self.lista_productos.items():
            print(f"Lista {key}:")
            lista.mostrar_productos()
            print()
