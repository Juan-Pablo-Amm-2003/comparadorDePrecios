# mvc/models.py

class ListaProductos:
    def __init__(self, nombre_archivo):
        self.nombre_archivo = nombre_archivo
        self.productos = self.cargar_productos()

    def cargar_productos(self):
        try:
            with open(self.nombre_archivo, 'r') as archivo:
                productos = {}
                for linea in archivo:
                    linea = linea.strip()
                    if linea:
                        partes = linea.split(' - ')
                        if len(partes) == 2:
                            nombre = partes[0].strip()
                            precio_str = partes[1].replace('$', '').replace(',', '').strip()
                            try:
                                precio = float(precio_str)
                                productos[nombre] = precio
                            except ValueError:
                                print(f"Advertencia: Ignorando línea mal formada en {self.nombre_archivo}: {linea}")
                        else:
                            print(f"Advertencia: Ignorando línea mal formada en {self.nombre_archivo}: {linea}")
                return productos
        except FileNotFoundError:
            print(f"El archivo {self.nombre_archivo} no existe. Creando uno nuevo.")
            return {}

    def guardar_productos(self):
        with open(self.nombre_archivo, 'w') as archivo:
            for producto, precio in self.productos.items():
                archivo.write(f"{producto} - ${precio}\n")

    def comparar_producto(self, producto):
        return self.productos.get(producto, None)

    def agregar_producto(self, producto, precio):
        self.productos[producto] = precio
        self.guardar_productos()
        print(f"Producto {producto} agregado correctamente.")

    def modificar_precio(self, producto, nuevo_precio):
        if producto in self.productos:
            self.productos[producto] = nuevo_precio
            self.guardar_productos()
            print(f"Precio de {producto} modificado correctamente.")
        else:
            print(f"El producto {producto} no existe en la lista.")

    def mostrar_productos(self):
        for producto, precio in self.productos.items():
            print(f"{producto}: ${precio}")
