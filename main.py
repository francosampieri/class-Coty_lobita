"""- Si se asigna un valor a una variable fuera de rango (mayor de lo establecido) ¿Qué 
ocurre? ¿Existe alguna forma de resolverlo? Ejemplifique. """
"""EJERCICIO 2"""
#La mejor forma de pedir un valor dentro de un rango es utilizar un bucle while que se repita hasta que el usuario ingrese un valor correcto.
numero_usuario = int(input("Ingresa un numero entre 2 y 10"))
while numero_usuario > 10 or numero_usuario < 2: 
    numero_usuario = int(input("ERROR: Ingresa un numero entre 2 y 10"))