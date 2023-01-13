# Escribir un programa que almacene la cadena de caracteres contraseña en una variable, 
# pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.

passw=input("Ingrese la contraseña: ")
password="huevofrito"
while passw != password:
    print("Contraseña invalida intenta de nuevo")
    passw=input("Ingrese la contraseña: ")
