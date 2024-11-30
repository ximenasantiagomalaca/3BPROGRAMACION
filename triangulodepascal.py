print("hecho por Ximena Santiago Malaca")
def triangulo_pascal(n):
    # Creamos una lista vacía que almacenará las filas del Triángulo de Pascal
    tri_pascal = []
    
    for i in range(n):
        # Inicializamos la fila con un 1
        fila = [1] * (i + 1)
        
        # Llenamos los valores intermedios de la fila, si no es la primera o la última posición
        for j in range(1, i):
            fila[j] = tri_pascal[i - 1][j - 1] + tri_pascal[i - 1][j]
        
        # Añadimos la fila al Triángulo de Pascal
        tri_pascal.append(fila)
    
    return tri_pascal

def imprimir_triangulo_pascal(tri_pascal):
    for fila in tri_pascal:
        print(" ".join(map(str, fila)).center(len(tri_pascal[-1]) * 3))

# Solicitar el número de filas
n = int(input("Ingrese el número de filas del Triángulo de Pascal: "))

# Llamar a la función para generar el Triángulo de Pascal
triangulo = triangulo_pascal(n)

# Imprimir el Triángulo de Pascal
imprimir_triangulo_pascal(triangulo)
