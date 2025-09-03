"""6- De la siguiente cadena “La lluvia en Mendoza es escasa” indique cual es el tamaño
de la cadena es decir su número de caracteres."""
longitud = len ("La lluvia en Mendoza es escasa ")
print  ("la lluvia en Mendoza es escasa tiene" , longitud , "caracteres" )
"""14_
En Python no existe la misma distinción explícita entre tipos por valor y tipos por referencia como en Java
 en python Todo es un objeto, Cuando asignas una variable, en realidad estás guardando una referencia a un objeto en memoria, no el objeto mismo.
Sin embargo, el comportamiento de esa referencia depende de si el objeto es mutable o inmutable.
- Objetos inmutables
 -int, float, bool, str, tuple, No se pueden modificar después de creados. Al cambiar su valor, en realidad se crea un nuevo objeto y la variable apunta a él.
- Objetos mutables
 -list, dict, set, objetos definidos por el usuario, se pueden modificar en memoria, Si varias variables apuntan al mismo objeto mutable, los cambios se reflejan en todas.
Python no tiene variables estrictamente "por valor" o "por referencia" como Java, Lo que sí tiene es un modelo de asignación por referencia a objetos, y el comportamiento final depende de si el objeto es mutable (parece referencia) o inmutable (parece valor)."""
"""11_ 
 Pedir dos palabras por teclado, indicar si son iguales"""
palabra1 = input("Escribe la primera palabra: ")
palabra2 = input("Escribe la segunda palabra: ")

if palabra1 == palabra2:
    print("Las palabras SON iguales.")
else:
    print("Las palabras NO son iguales.")