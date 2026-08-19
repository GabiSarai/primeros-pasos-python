secret=input("ingrese su palabra para salir del encierro:")

while True: 
    if secret == "chupacabra":
        break
    secret = input("JA JA! siga intentando con otra palabra ")
    
print("has dejado el bucle con exito")
