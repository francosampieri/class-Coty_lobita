"""Codifique un algoritmo que solicite el ingreso de un numero de 3 dígitos (100 - 999)
y por medio del uso de las operaciones matemáticas módulo 10 y división por 10
efectué la suma de los 3 dígitos del número. Ejemplo ingreso 563, salida del algoritmo
14. Plantee el algoritmo planteando métodos para su resolución."""
def leer_numero():
    num=int(input("Ingrese un numero de 3 digitos: "))
    while not 100<=num<=999:
        num=int(input("ERROR: Ingrese un numero de 3 digitos: "))
    return num

def descompnoner_numero(num):
    d1=num%10
    num=num//10
    d2=num%10
    num=num//10
    d3=num%10
    return d1,d2,d3
def sumar_numeros(d1,d2,d3):
    suma=d3+d2+d1
    return suma

   
num=leer_numero()
d1,d2,d3=descompnoner_numero(num)
suma=sumar_numeros(d1,d2,d3)
print(f"La suma de los digitos del numero {num} es {suma}")