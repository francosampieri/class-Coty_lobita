"""EJERCICIO 2"""
#La mejor forma de pedir un valor dentro de un rango es utilizar un bucle while que se repita hasta que el usuario ingrese un valor correcto.
numero_usuario = int(input("Ingresa un numero entre 2 y 10 "))
while numero_usuario > 10 or numero_usuario < 2: 
    numero_usuario = int(input("ERROR: Ingresa un numero entre 2 y 10 "))

"""EJERCICIO 8"""
cadena_usuario = input("Ingresa una cadena y cambiare sus \"a\" por \"e\": ")
cadena_nueva = ""
for letra in cadena_usuario:
    if letra == "a": cadena_nueva += "e"
    else: cadena_nueva += letra
print (cadena_nueva)

"""EJERCICIO 9"""
cadena = "La lluvia en Mendoza es escasa"
for letra in cadena:
    print (ord(letra), end=(" "))

"""EJERCICIO 15"""
#Esas lineas de codigo van a imprimir None. Un nonetype es un tipo de dato que se usa normalmente como un valor por defecto o para indicar que algo fallo o no se encontró.

"""EJERCICIO 17"""