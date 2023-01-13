# Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y
# muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.

CInvertir=float(input("Ingrese la cantidad de Dinero a invertir: "))
InteresAnual=float(input("Ingrese Cantidad de Interes Anual: "))
Nyears=int(input("Ingrese el numero de años: "))

for i in range(1,Nyears+1):
    CInvertir=CInvertir*1+InteresAnual/100
    print("Para el primer Año ",i, "Obtuvo un interes de", round(CInvertir,2))