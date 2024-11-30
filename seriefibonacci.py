print("hecho por Ximena Santiago Malaca")
def fibonacci(n):
    # Inicializamos los dos primeros términos de la secuencia
    a, b = 0, 1
    # Creamos una lista para almacenar la secuencia
    fib_sequence = []
    
    # Generamos los términos de la serie hasta el número n
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b  # Actualizamos los valores de a y b
    
    return fib_sequence

# Solicitar el número de términos de la serie
n = int(input("Ingrese el número de términos de la serie de Fibonacci: "))

# Llamamos a la función y mostramos el resultado
print(f"Serie de Fibonacci con {n} términos: {fibonacci(n)}")
