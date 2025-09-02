
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
