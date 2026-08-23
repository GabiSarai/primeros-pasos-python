c0 = int(input("ingrese numero entero mayor a 1: "))
pasos = 0

while c0 != 1:
  print(c0)
  pasos += 1
  if c0 % 2 ==0:
    c0 = c0//2
  else:
    c0 = 3*c0 + 1

print(c0)
print("pasos: ", pasos)
