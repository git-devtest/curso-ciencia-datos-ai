''' 
🐍 1. Introducción a Python
Python es un lenguaje de programación de alto nivel,
interpretado y multipropósito.

🔹 Sintaxis básica
Python es conocido por su sintaxis limpia y legible. 
No usa llaves {} ni punto y coma ;, 
sino indentación para definir bloques de código.
'''

# Esto es un comentario
print("Hola, mundo")  # Imprime texto en consola

'''
🔹 Variables
No necesitas declarar el tipo de variable explícitamente.
'''
# Variables y tipos de datos
nombre = "Jhon"     # Cadena de texto
edad = 30           # Entero
altura = 1.75       # Flotante
pi = 3.1416         # Flotante
activo = True       # Booleano
lenguajes = ["Python", "Java", "C++"]           # Lista
diccionario = {"nombre": "Jhon", "edad": 30}    # Diccionario

# Imprimir variables
print(nombre, edad, altura, pi, activo)

'''
Tipos de datos en Python
Python tiene varios tipos de datos básicos que puedes usar para almacenar información.
Aquí hay una tabla con algunos de los más comunes:
----------------------------------------------------------------------
| Tipo   | Ejemplo              | Descripción                        |
|--------|----------------------|------------------------------------|
| int    | 42                   | Enteros                            |
| float  | 3.14                 | Números decimales                  |
| str    | "Hola"               | Cadenas de texto                   |
| bool   | True, False          | Valores booleanos                  |
| list   | [1, 2, 3]            | Lista ordenada de elementos        |
| dict   | {"clave": "valor"}   | Diccionario (clave-valor)          |
'''

'''
🔄 2. Estructuras de control: Condicionales
🔹 if, elif, else
Permiten ejecutar código según condiciones.

🔹 Operadores comunes
Se usan para comparar valores y devolver True o False.
    == igual
    != distinto
    < menor que, > mayor que, <= menor o igual, >= mayor o igual
    and y, or o, not, no
'''
edad = 16
bandera = False
print(bandera)

if edad < 18:
    print("Eres menor de edad")
    print(not bandera)  # Cambia el valor de bandera a True
elif edad < 65:
    print("Eres adulto")
    print(not bandera)  # Cambia el valor de bandera a True
elif edad < 100 and edad >= 65:
    print("Eres adulto mayor")
    print(not bandera)  # Cambia el valor de bandera a True
else:
    print("Eres adulto mayor")
    print(not bandera)  # Cambia el valor de bandera a True

'''
🔁 3. Bucles y comprensión de listas
🔹 Bucle for
Recorre elementos de una secuencia.
'''
frutas = ["manzana", "banana", "pera"]

for fruta in frutas:
    print(fruta)

'''
🔹 Bucle while
Se ejecuta mientras la condición sea verdadera.
'''
contador = 0

while contador < 5:
    print("Contador:", contador)
    contador += 1

'''
🔹 range()
Función útil para generar secuencias numéricas.
'''
for i in range(3):  # 0, 1, 2
    print("Iteración", i)

'''
🔹 Comprensión de listas
Forma compacta de crear listas.
'''
cuadrados = [x**2 for x in range(5)]
print(cuadrados)  # [0, 1, 4, 9, 16]

# También puedes incluir condicionales:
pares = [x for x in range(10) if x % 2 == 0]
print(pares)  # [0, 2, 4, 6, 8]
