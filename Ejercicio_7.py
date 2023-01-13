# Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.

numero=int(input("Ingrese un numero para generar la tabla de multiplicar: "))

for i in range(11):
    print(numero,"*",i,"=",numero*i)
