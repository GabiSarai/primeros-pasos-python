edad_1 = int(input("ingrese la edad de la primera persona:"))
edad_2 = int(input("ingrese la edad de la segunda persona:"))
edad_3 = int(input("ingrese la edad de la tercera persona:"))
edad_mayor = edad_1

if edad_2 > edad_1:
    edad_mayor = edad_2
    
if edad_3 > edad_mayor:
    edad_mayor = edad_3
    
print("la persona de mayor edad tiene", edad_mayor, "años")
