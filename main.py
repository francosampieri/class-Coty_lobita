
#Ejercicio 4
def dinero(monto):
    billetes = [200, 100, 50, 20, 10, 5, 2, 1]
    monedas = [0.50, 0.25, 0.10, 0.05]
    
    entero = int(monto)
    
    # Billetes
    for i in billetes:
        cantidad = entero // i
        entero %= i
        if cantidad > 0:
            print(f"{cantidad} billete(s) de {i}")
    
    # Monedas
    decimal = round((monto - int(monto)) * 100)
    for h in monedas:
        valor = int(h * 100)
        cantidad = decimal // valor
        decimal %= valor
        if cantidad > 0:
            print(f"{cantidad} moneda(s) de {h}")

monto = float(input("Ingrese el monto de dinero: "))
dinero(monto)

#Ejercicio 7
contador = 0
vocale = ["a", "e", "i", "o", "u"]
cadena = input(" ingrese una cadena")
can_num = (cadena)
for i in cadena.lower():
    if i in vocale:
        contador +=1
print( "cantidad de vocales", contador)
print("longitud palabra" ,can_num)


#Ejercicio 12
palabra = "Hipopotamo"
for i in range((palabra)):
    if i == 3 or i == 4: 
        print(palabra[i])
#Ejercicio 20
class Fraccion:
    def __init__(self, numerador,denominador):
        self.numerador = numerador
        self.denominador = denominador
    @staticmethod
    def SumarFracciones(f1, f2):
        numerador = f1.numerador * f2.denominador + f2.numerador * f1.denominador
        denominador = f1.denominador * f2.denominador
        return Fraccion(numerador, denominador)

    @staticmethod
    def RestaFracciones(f1, f2):
        numerador = f1.numerador * f2.denominador - f2.numerador * f1.denominador
        denominador = f1.denominador * f2.denominador
        return Fraccion(numerador, denominador)

    @staticmethod
    def MultiplicacionFracciones(f1, f2):
        numerador = f1.numerador * f2.numerador
        denominador = f1.denominador * f2.denominador
        return Fraccion(numerador, denominador)

    @staticmethod
    def DivisionFracciones(f1, f2):
        numerador = f1.numerador * f2.denominador
        denominador = f1.denominador * f2.numerador
        return Fraccion(numerador, denominador)
class OperacionesFracciones:
    def main():
        num1 = int(input("Ingrese el numerador para la fraccion 1"))
        num2 = int(input("Ingrese el denominador para la fraccion 1"))
        num3 = int(input("Ingrese el numerador para la fraccion 2"))
        num4 = int(input("Ingrese el denominador para la fraccion 2"))
        
        Fraccion1 = Fraccion(num1,num2)
        Fraccion2 = Fraccion(num3,num4)
        
        ResultadoSuma = Fraccion.SumarFracciones(Fraccion1, Fraccion2) 
        ResultadoResta = Fraccion.RestaFracciones(Fraccion1,Fraccion2)
        ResultadoMultiplicacion = Fraccion.MultiplicacionFracciones(Fraccion1,Fraccion2)
        ResultadoDivision = Fraccion.DivisionFracciones(Fraccion1,Fraccion2)
        print("RESULTADO SUMA DE FRACCION", ResultadoSuma)
        print("RESULTADO RESTA DE FRACCION", ResultadoResta)
        print("RESULTADO MULTIPLICACION DE FRACCION", ResultadoMultiplicacion)
        print("RESULTADO DIVISION DE FRACCION", ResultadoDivision)
OperacionesFracciones.main()

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

