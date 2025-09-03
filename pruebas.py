"""Recorre la cadena del ejercicio 6 y transforma cada carácter a su código ASCII. 
Muéstralos en línea recta, separados por un espacio entre cada carácter"""
cadena = "La lluvia en Mendoza es escasa"
for letra in cadena:
    print (ord(letra), end=(" "))