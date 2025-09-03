#Ejercicio1
valorDecimal = float(input("Ingrese un número decimal: "))

print("\n--- Resultados del CASTEO ---")

#entero
valorEntero = int(valorDecimal)
print("Entero (int):", valorEntero)

#texto
valorTexto = str(valorDecimal)
print("Texto (str):", valorTexto, " -> Tipo:", type(valorTexto))

#booleano
valorBooleano = bool(valorDecimal)
print("Booleano (bool):", valorBooleano)

#float 
valorFlotante = float(valorDecimal)
print("Flotante (float):", valorFlotante)

#redondear
valorRedondeado = round(valorDecimal)
print("Redondeado (round):", valorRedondeado)

#Ejercicio5 

texto = input("Ingrese una cadena: ") 

texto_sin_espacio = texto.replace(" " , "")

print("Cadena sin espacio " , texto_sin_espacio)


#Ejercicio10

def mayuscula(texto):
    return texto.upper()

def minuscula(texto):

    return texto.lower()




texto = input("Ingrese una cadena: ")

print("Opciones: ")
print("1- Convertir a Mayuscula ")
print("2- Convertir a Minuscula ")

opcion = input("Ingrese la opcion deseada ")



if opcion == "1" :
    resultado = mayuscula(texto)
    print("Cadena en maysucla: ",resultado)

elif opcion == "2" :
    resultado = minuscula(texto)
    print("Cadena en minuscula: ",resultado)


else:
    print("Opcion no valida. Debe ingresar 1 o 2!")

    #Ejercicio13 


cadena1 = input("Ingresa la primera cadena: ")
cadena2 = input("Ingresa la segunda cadena: ")


if cadena2 in cadena1:
    print("La segunda cadena se encuentra dentro de la primera.")
else:
    print("La segunda cadena NO se encuentra dentro de la primera.")
