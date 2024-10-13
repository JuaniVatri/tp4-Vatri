"""Ejercicio Final
Sistema de Gestión de Inventario de Tienda
Descripción:
Una tienda de tecnología necesita llevar un registro de su inventario. Cada producto tiene asociado un código, una descripción, y un precio. Además, el sistema debe ser capaz de:
1. Mostrar todos los productos disponibles.
2. Buscar un producto por su código.
3. Modificar el precio de un producto.
4. Eliminar un producto del inventario.
5. Mostrar todos los productos cuyo precio esté en un rango dado por el usuario.
Para realizar este ejercicio, usa las siguientes estructuras:
 Tuplas para almacenar los detalles de cada producto (código, descripción, precio).
 Diccionarios para almacenar el inventario, donde el código del producto será la clave y el valor será una tupla con la descripción y el precio.
Instrucciones:
1. Crear un diccionario que contenga el inventario inicial con al menos 5 productos.
o Cada clave será un código de producto (ej. "A001", "A002").
o Cada valor será una tupla con la descripción del producto y su precio.
2. Implementar las siguientes funciones:
o mostrar_inventario(inventario): Muestra todos los productos del inventario con su código, descripción y precio.
o buscar_producto(inventario, codigo): Busca un producto por su código. Si existe, muestra su descripción y precio.
o modificar_precio(inventario, codigo, nuevo_precio): Modifica el precio de un producto dado su código.
o eliminar_producto(inventario, codigo): Elimina un producto del inventario usando su código.
o productos_por_rango_de_precio(inventario, min_precio, max_precio): Muestra todos los productos cuyo precio esté entre min_precio y max_precio.
Ejemplo de Inventario: inventario = { "A001": ("Laptop", 1500), "A002": ("Mouse", 25), "A003": ("Teclado", 45), "A004": ("Monitor", 300), "A005": ("Impresora", 120) }
Ejemplo de salida esperada:
 Mostrar inventario: mostrar_inventario(inventario)
Salida: Código: A001, Descripción: Laptop, Precio: $1500 Código: A002, Descripción: Mouse, Precio: $25 Código: A003, Descripción: Teclado, Precio: $45 Código: A004, Descripción: Monitor, Precio: $300 Código: A005, Descripción: Impresora, Precio: $120
 Buscar producto por código: buscar_producto(inventario, "A003")
Salida: Producto encontrado: Teclado, Precio: $45
 Modificar el precio de un producto: modificar_precio(inventario, "A004", 350)
Salida: El precio del producto con código A004 ha sido actualizado a $350
 Eliminar un producto del inventario: eliminar_producto(inventario, "A002")
Salida: El producto con código A002 ha sido eliminado del inventario.
 Mostrar productos dentro de un rango de precios: productos_por_rango_de_precio(inventario, 100, 500)
Salida: Productos en el rango de precio entre $100 y $500: Código: A004, Descripción: Monitor, Precio: $350 Código: A005, Descripción: Impresora, Precio: $120"""
# Inventario inicial
inventario = {
    "A001": ("Laptop", 1500),
    "A002": ("Mouse", 25),
    "A003": ("Teclado", 45),
    "A004": ("Monitor", 300),
    "A005": ("Impresora", 120)
}

def mostrar_inventario(inventario):
    """Muestra todos los productos del inventario con su código, descripción y precio."""
    for codigo, (descripcion, precio) in inventario.items():
        print(f"Código: {codigo}, Descripción: {descripcion}, Precio: ${precio}")

def buscar_producto(inventario, codigo):
    """Busca un producto por su código. Si existe, muestra su descripción y precio."""
    producto = inventario.get(codigo)
    if producto:
        descripcion, precio = producto
        print(f"Producto encontrado: {descripcion}, Precio: ${precio}")
    else:
        print("Producto no encontrado.")

def modificar_precio(inventario, codigo, nuevo_precio):
    """Modifica el precio de un producto dado su código."""
    if codigo in inventario:
        descripcion, _ = inventario[codigo]
        inventario[codigo] = (descripcion, nuevo_precio)
        print(f"El precio del producto con código {codigo} ha sido actualizado a ${nuevo_precio}")
    else:
        print("Producto no encontrado.")

def eliminar_producto(inventario, codigo):
    """Elimina un producto del inventario usando su código."""
    if codigo in inventario:
        del inventario[codigo]
        print(f"El producto con código {codigo} ha sido eliminado del inventario.")
    else:
        print("Producto no encontrado.")

def productos_por_rango_de_precio(inventario, min_precio, max_precio):
    """Muestra todos los productos cuyo precio esté entre min_precio y max_precio."""
    print(f"Productos en el rango de precio entre ${min_precio} y ${max_precio}:")
    for codigo, (descripcion, precio) in inventario.items():
        if min_precio <= precio <= max_precio:
            print(f"Código: {codigo}, Descripción: {descripcion}, Precio: ${precio}")


#ejemplos de uso
mostrar_inventario(inventario)
print()
buscar_producto(inventario, "A003")
print()
modificar_precio(inventario, "A004", 350)
print()
eliminar_producto(inventario, "A002")
print()
productos_por_rango_de_precio(inventario, 100, 500)