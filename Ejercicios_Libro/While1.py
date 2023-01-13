#Escriba un programa que pregunte una y otra vez si desea continuar con el programa, siempre que se conteste exactamente sí 
# (en minúsculas y con tilde).

# frase="si"
# while frase=="si":
#     frase=input("Desea continuar ")
#     frase=frase.lower()
#     if frase !="si":
#         break


# contador=0
# while contador<5:
#     contador=contador+1
#     print(contador)
# print("Contador ya no es menor a 5, termino el programa")



# count = 0
# while(count < 5):
#     count = count+1
#     print("Iteración número {}".format(count))
# else:
#     print("Bucle while finalizado")


# Leer números enteros de teclado, hasta que el usuario ingrese el 0. Finalmente, mostrar la sumatoria de todos los números ingresados.
#num=input("Ingrese un numero ")
# n=True
# conta=0
# while n:
#     num=int(input( "Ingrese un numero "))
#     conta=conta+num
#     if num==0:
#         print("Ingresó el numero cero, El programa termino Adios ")
#         n=False
#         break
# print(conta)


# Leer números enteros de teclado, hasta que el usuario ingrese el 0. Finalmente, mostrar la sumatoria de todos 
# los números positivos ingresados.
# n=True
# conta=0
# while n:
#     num=int(input( "Ingrese un numero "))
#     if num>0:
#         conta=conta+num
#     if num==0:
#         print("Ingresó el numero cero, El programa termino Adios ")
#         n=False
#         break
# print(conta)



# Leer números enteros positivos de teclado, hasta que el usuario ingrese el 0. Informar cuál fue el mayor número ingresado.
# n=True
# conta=0
# while n:
#     num=int(input( "Ingrese un numero "))
#     if num>conta:
#         conta=num
#     if num==0:
#         print("Ingresó el numero cero, El programa termino Adios ")
#         n=False
#         break
# print( "El numero mayor es: ", conta )


# Leer un número entero positivo desde teclado e imprimir la suma de los dígitos que lo componen.
# num=int(input("Ingrese un numero "))

# n=True

# while n:
#     res=num*(num+1)/2
#     break
# print(res)


# Solicitar al usuario que ingrese números enteros positivos y, por cada uno, imprimir la suma de los dígitos que lo componen. 
# La condición de corte es que se ingrese el número -1. Al finalizar, mostrar cuántos de los números ingresados por el usuario 
# fueron números pares.

# n=True
# cont=0
# list2=[]
# list=[]
# while n:
#     num=int(input("Ingrese un numero "))
#     if num>-1:
#         res=num*(num+1)/2
#         list.append(res)
#         if num%2 ==0:
#             list2.append(num)
#     else:
#         break
# print(list, "Los numero pares ingresados son ", list2)
# #print(req)



#Mostrar un menú con tres opciones: 1- comenzar programa, 2- imprimir listado, 3-finalizar programa. A continuación, 
#el usuario debe poder seleccionar una opción (1, 2 ó 3). Si elige una opción incorrecta, informarle del error. El menú se 
#debe volver a mostrar luego de ejecutada cada opción, permitiendo volver a elegir. Si elige las opciones 1 ó 2 se imprimirá un texto. 
#Si elige la opción 3, se interrumpirá la impresión del menú y el programa finalizará.

# print("Bienvenido a nuestro programa ")
# print("Ingrese el numero correspondiente a la acccion que necesite ")
# print("Ejemplo: escriba uno 1 para comenzar el programa, dos 2 para imprimir y tres 3 para finalizar programa ")
# print(" 1- Comenzar programa ")
# print(" 2- Imprimir listado ")
# print(" 3- finalizar programa ")
# start=int(input(" Ingrese el numero de su eleccion "))
# n=True
# while n:
#     if start==1:
#         print("iniciando programa de autodestruccion ")
#         n=False
#     elif start==2:
#         print("Se esta imprimiendo el listado del programa de autodestruccion ")
#         n=False
#     elif start==3:
#         break
#     else:
#         print("el numero ingresado no corresponde a ninguna opcion por favor ingrese un numero correcto")



#Solicitar al usuario el ingreso de una frase y de una letra (que puede o no estar en la frase). Recorrer la frase, carácter a carácter, 
#comparando con la letra buscada. Si el carácter no coincide, indicar que no hay coincidencia en esa posición (imprimiendo la posición) 
#y continuar. Si se encuentra una coincidencia, indicar en qué posición se encontró y finalizar la ejecución.

