'''
📘 2. Funciones y Excepciones en Python
🔹 Funciones en Python

Las funciones permiten reutilizar código y organizarlo mejor.
'''

# ✅ Definición básica
def saludar(nombre):
    return f"Hola, {nombre}!"

print(saludar("Jhon"))  # "Hola, Jhon!"

# ✅ Argumentos y retorno
def sumar(a, b):
    resultado = a + b
    return resultado

print(sumar(3, 5))  # 8

# ✅ Puedes usar parámetros por defecto
def saludar(nombre="Jhon"):
    return f"Hola, {nombre}!"

print(saludar())       # "Hola, Jhon!"
print(saludar("Ana"))  # "Hola, Ana!"

# ✅ Y también argumentos nombrados
def potencia(base, exponente=2):
    return base ** exponente

print(potencia(3))       # 9
print(potencia(3, 3))    # 27

# 🔹 Manejo de excepciones (try-except)
# Sirve para evitar que el programa se detenga por errores.
try:
    numero = int(input("Ingresa un número: "))
    print("Número válido:", numero)
except ValueError:
    print("¡Eso no es un número!")

# También puedes capturar múltiples errores:
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("No puedes dividir por cero.")
except Exception as e:
    print(f"Ocurrió un error: {e}")

# Puedes usar `finally` para ejecutar código que siempre se ejecute, 
# sin importar si hubo error o no.
try:
    archivo = open("archivo.txt", "r")
    contenido = archivo.read()
except FileNotFoundError:
    print("El archivo no existe.")

# 🧪 Práctica: Funciones para calcular áreas
def area_cuadrado(lado):
    return lado ** 2

def area_rectangulo(base, altura):
    return base * altura

def area_circulo(radio):
    import math
    return math.pi * radio ** 2

# Ejemplo de uso
print("Área cuadrado:", area_cuadrado(4))
print("Área rectángulo:", area_rectangulo(5, 3))
print("Área círculo:", area_circulo(2))
