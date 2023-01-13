# Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo 
# como el de más abajo, de altura el número introducido.
number=int(input("Ingrese un numero entero positivo: "))
for i in range(number):
    for n in range(i+1):
        print("*", end=" ")
    print(" ")

for i in range(number):
    print("*"*(i+1))