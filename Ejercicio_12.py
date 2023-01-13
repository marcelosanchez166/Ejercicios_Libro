# Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por 
# pantalla el número de veces que aparece la letra en la frase.

Palabra=input("Ingrese una palabra: ")
letra=input("Ingrese una letra para ver si existe en la palabra ingresada: ")
count=0
for i in Palabra:
    if i ==letra:
        count=count+1
print("Numero de veces que se repite la letra: ", count)

