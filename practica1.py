cont = input("ingrese su codigo: ")
print("su codigo incriptado es:", end= "")
for i in cont:
    if i == "0":
        print("x", end="")
        continue
    if i == "1":
        print("y", end="")
        continue
    print(i, end="")
