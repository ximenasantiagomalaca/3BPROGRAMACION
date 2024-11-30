# Definimos la base de datos como una lista vacía
print("Hecho por Ximena Santiago Malaca y Dulce Yareli Cruz Santos")
base_de_datos = []

# Contraseña predefinida
CONTRASENA = "maquillaje123"

# Función para solicitar contraseña
def verificar_contraseña():
    intento = input("Ingrese la contraseña para acceder: ")
    if intento == CONTRASENA:
        print("Contraseña correcta.\n")
        return True
    else:
        print("Contraseña incorrecta. Intente nuevamente.\n")
        return False

# Función para agregar un nuevo producto
def agregar_producto():
    print("Agregar nuevo producto")
    nombre = input("Nombre del producto: ")
    marca = input("Marca: ")
    tipo = input("Tipo de producto (base, lipstick, etc.): ")
    color = input("Color: ")
    precio = float(input("Precio: "))
    cantidad = int(input("Cantidad en stock: "))
    fecha_vencimiento = input("Fecha de vencimiento (dd/mm/aaaa): ")
    categoria = input("Categoría (para rostro, ojos, labios, etc.): ")
    descripcion = input("Descripción breve del producto: ")
    codigo_producto = input("Código del producto: ")
    
    # Agregar el producto como un diccionario a la base de datos
    producto = {
        "nombre": nombre,
        "marca": marca,
        "tipo": tipo,
        "color": color,
        "precio": precio,
        "cantidad": cantidad,
        "fecha_vencimiento": fecha_vencimiento,
        "categoria": categoria,
        "descripcion": descripcion,
        "codigo_producto": codigo_producto
    }
    
    base_de_datos.append(producto)
    print("Producto agregado exitosamente.\n")

# Función para consultar (mostrar) los productos
def consultar_productos():
    if not base_de_datos:
        print("No hay productos en la base de datos.\n")
    else:
        for producto in base_de_datos:
            print("===================================")
            for clave, valor in producto.items():
                print(f"{clave.capitalize()}: {valor}")
            print("===================================")
        print("\n")

# Función para modificar un producto
def modificar_producto():
    codigo = input("Ingrese el código del producto a modificar: ")
    encontrado = False
    
    for producto in base_de_datos:
        if producto["codigo_producto"] == codigo:
            print("Producto encontrado. ¿Qué deseas modificar?")
            producto["nombre"] = input(f"Nuevo nombre (actual: {producto['nombre']}): ")
            producto["marca"] = input(f"Marca (actual: {producto['marca']}): ")
            producto["tipo"] = input(f"Tipo (actual: {producto['tipo']}): ")
            producto["color"] = input(f"Color (actual: {producto['color']}): ")
            producto["precio"] = float(input(f"Precio (actual: {producto['precio']}): "))
            producto["cantidad"] = int(input(f"Cantidad (actual: {producto['cantidad']}): "))
            producto["fecha_vencimiento"] = input(f"Fecha de vencimiento (actual: {producto['fecha_vencimiento']}): ")
            producto["categoria"] = input(f"Categoría (actual: {producto['categoria']}): ")
            producto["descripcion"] = input(f"Descripción (actual: {producto['descripcion']}): ")
            print("Producto modificado exitosamente.\n")
            encontrado = True
            break
    
    if not encontrado:
        print("Producto no encontrado.\n")

# Función para eliminar un producto
def eliminar_producto():
    codigo = input("Ingrese el código del producto a eliminar: ")
    encontrado = False
    
    for i, producto in enumerate(base_de_datos):
        if producto["codigo_producto"] == codigo:
            del base_de_datos[i]
            print("Producto eliminado exitosamente.\n")
            encontrado = True
            break
    
    if not encontrado:
        print("Producto no encontrado.\n")

# Función principal del programa
def menu():
    while True:
        print("Menú de opciones:")
        print("1. Agregar producto")
        print("2. Consultar productos")
        print("3. Modificar producto")
        print("4. Eliminar producto")
        print("5. Salir")
        
        opcion = input("Seleccione una opción (1-5): ")
        
        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            consultar_productos()
        elif opcion == "3":
            modificar_producto()
        elif opcion == "4":
            eliminar_producto()
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intente de nuevo.\n")

# Ejecución del programa
if verificar_contraseña():
    menu()
