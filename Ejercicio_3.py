# Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número
# separados por comas.

number=int(input("Ingrese un numero entero: "))
for i in range(number+1):
    if i % 2 != 0:
        print(i, end = ",")



