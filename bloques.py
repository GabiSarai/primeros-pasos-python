bloques = int(input("Ingresa el número de bloques: "))
capa_actual = 1
altura = 0

while bloques >= capa_actual:
    altura += 1
    bloques -= capa_actual
    capa_actual += 1
      
print("La altura de la pirámide:", altura)
