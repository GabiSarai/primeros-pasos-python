print("BIENVENIDO DE NUEVO BIOLOGO MARINO\n")
temp = float(input("ingrese Temperatura del area (°C): "))
salin = float(input("ingrese Salinidad del area (PSU): "))
biolumin = input("presencio bioluminiscencia en el area?: ")
if temp >= 0 and temp <= 4 and salin >= 34.0 and salin <= 36.0:
    print("Estado del entorno: Zona abismal estandar")
elif temp > 4 and biolumin == 'si':
    print("Estado del entorno: Zona de Resurgencia Termal\nALERTA: Entorno de alta actividad energética detectado")
elif temp < 0:
    print("Estado del entorno: Zona glacial extrema\nALERTA: Entorno de frío extremo detectado")
else:
    print("ZONA DE ANOMALIA DESCONOCIDA")
