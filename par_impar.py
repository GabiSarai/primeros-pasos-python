#primer uso del bucle while
#se lee una secuencia de numeros
#y cuenta cuantos numeros son pares e impares

num_pares = 0
num_impares = 0
numero = int(input("introduzca un numero o coloque 0 para detener: "))

# al colocar 0 termina la ejecucion del bucle
while numero != 0:
    if numero %2 == 1:
        num_impares += 1
    else:
        num_pares += 1
    #lee el siguiente numero
    numero = int(input("introduzca un numero o coloque 0 para detener: "))

#imprime resultado final del conteo
print("el conteo de numeros pares es de: ", num_pares)
print("el conteo de numeros impares es de: ", num_impares)
