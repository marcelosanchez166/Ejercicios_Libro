# Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).


edad=int(input("Ingresa tu edad: "))
year=2022
nacimiento=year-edad
print("nacimiento ",nacimiento)
for i in range(edad+1):
    print(nacimiento+i)