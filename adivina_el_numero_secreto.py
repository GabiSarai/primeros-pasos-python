#se asigna el numero que la persona tiene que ingresar para que el bucle se cierre
num_secreto = 77
print(
"""
+=======================================+
| ¡Bienvenido a mi juego, muggle!       |
| Introduce un número entero            |
| y adivina qué número he               |
| elegido para ti.                      |
|¿Sabras cuál es el número secreto?     |
+=======================================+
""")
num1 = int(input("ingrese su primer intento: "))

# 77 es el numero (o el que eligas) para que el bucle pare
while num1 != num_secreto:
    print("¡Ja, ja! ¡Estás atrapado en mi bucle!")
    num1 = int(input("\ningrese siguiente intento: "))
else:
    print("¡Bien hecho, muggle! Eres libre ahora.")
