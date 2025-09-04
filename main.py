def ejercicio_1():
    valorDecimal = float(input("Ingrese un número decimal: "))

    print("\n--- Resultados del CASTEO ---")

    #entero
    valorEntero = int(valorDecimal)
    print("Entero (int):", valorEntero)

    #texto
    valorTexto = str(valorDecimal)
    print("Texto (str):", valorTexto)

    #booleano
    valorBooleano = bool(valorDecimal)
    print("Booleano (bool):", valorBooleano)

    #float 
    valorFlotante = float(valorDecimal)
    print("Flotante (float):", valorFlotante)

    #redondear
    valorRedondeado = round(valorDecimal)
    print("Redondeado (round):", valorRedondeado)

def ejercicio_2():
    print("La mejor forma de pedir un valor dentro de un rango es utilizar un bucle while que se repita hasta que el usuario ingrese un valor correcto.")
    numero_usuario = int(input("Ingresa un numero entre 2 y 10 "))
    while numero_usuario > 10 or numero_usuario < 2: 
        numero_usuario = int(input("ERROR: Ingresa un numero entre 2 y 10 "))

def ejercicio_3():
    def leer_numero():
        num=int(input("Ingrese un numero de 3 digitos: "))
        while not 100<=num<=999:
            num=int(input("ERROR: Ingrese un numero de 3 digitos: "))
        return num

    def descomponer_numero(num):
        d1=num%10
        num=num//10
        d2=num%10
        num=num//10
        d3=num%10
        return d1,d2,d3
    def sumar_numeros(d1,d2,d3):
        suma=d3+d2+d1
        return suma

    #main
    num=leer_numero()
    d1,d2,d3=descomponer_numero(num)
    suma=sumar_numeros(d1,d2,d3)
    print(f"La suma de los digitos del numero {num} es {suma}")

def ejercicio_4():
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

def ejercicio_5():
    texto = input("Ingrese una cadena para removerle sus espacios: ") 
    texto_sin_espacio = texto.replace(" " , "")
    print("Cadena sin espacio" , texto_sin_espacio)

def ejercicio_6():
    longitud = len("La lluvia en Mendoza es escasa")
    print  ("La frase \"La lluvia en Mendoza es escasa\" tiene" ,longitud, "caracteres" )

def ejercicio_7():
    vocales = ["a", "e", "i", "o", "u"]
    cadena = input("Ingrese una cadena para contar sus vocales y longitud ")
    cant_num = len(cadena)
    contador = 0
    for i in cadena.lower():
        if i in vocales:
            contador +=1
    print("Cantidad de vocales:", contador)
    print("Longitud de palabra:", cant_num)

def ejercicio_8():
    cadena_usuario = input("Ingresa una cadena y cambiare sus \"a\" por \"e\": ")
    cadena_nueva = ""
    for letra in cadena_usuario:
        if letra == "a": cadena_nueva += "e"
        else: cadena_nueva += letra
    print (cadena_nueva)

def ejercicio_9():
    cadena = "La lluvia en Mendoza es escasa"
    for letra in cadena:
        print (ord(letra), end=(" "))
    print("") #para que el proximo ejercicio no empiece en la misma linea

def ejercicio_10():
    def convertir_mayuscula(texto):
        return texto.upper()

    def convertir_minuscula(texto):
        return texto.lower()

    texto = input("Ingrese una cadena: ")

    print("Opciones: ")
    print("1- Convertir a Mayuscula ")
    print("2- Convertir a Minuscula ")

    opcion = input("Ingrese la opcion deseada: ")
    while opcion != "1" and opcion != "2":
        print("ERROR: Ingrese una opcion correcta ")
        print("Opciones: ")
        print("1- Convertir a Mayuscula ")
        print("2- Convertir a Minuscula ")
        opcion = input("Ingrese la opcion deseada: ")


    if opcion == "1" :
        resultado = convertir_mayuscula(texto)
        print("Cadena en mayuscula:",resultado)
    else:
        resultado = convertir_minuscula(texto)
        print("Cadena en minuscula:",resultado)

def ejercicio_11():
    palabra1 = input("Escribe la primer palabra: ")
    palabra2 = input("Escribe la segunda palabra: ")

    if palabra1 == palabra2:
        print("Las palabras son iguales.")
    else:
        print("Las palabras no son iguales.")

def ejercicio_12():
    palabra = "Hipopotamo"
    for i in range(len(palabra)):
        if i == 3 or i == 4: 
            print(f"letra [{i+1}] = {palabra[i]}")

def ejercicio_13():
    cadena1 = input("Ingresa la primera cadena: ")
    cadena2 = input("Ingresa la segunda cadena: ")

    if cadena2 in cadena1:
        print("La segunda cadena se encuentra dentro de la primera.")
    else:
        print("La segunda cadena NO se encuentra dentro de la primera.")

def ejercicio_14():
    print("No, en python no existen variables variables de tipo referencia y por valor, como en Java o pseint. Solo hay objetos, y referencias a los mismos")

def ejercicio_15():
    print("Esas lineas de codigo van a imprimir None. Un nonetype es un tipo de dato que se usa normalmente como un valor por defecto o para indicar que algo fallo o no se encontró.")

def ejercicio_16():
    def contiene_num(cadena): 
        resultado= False
        for i in cadena:
            if i.isnumeric(): resultado= True
        if resultado: print(f"La cadena {cadena} contiene numeros")
        else: print (f"La cadena {cadena} no contiene numeros")
    contiene_num("hola2")

def ejercicio_17():
    #No encontramos la forma de pasar años a palabras sin usar librerias externas como num2word. (datetime no lo hace)
    from datetime import datetime
    class FuncionesPrograma:
        # Diccionarios para convertir números a texto
        dias = {
            1:"Uno", 2:"Dos", 3:"Tres", 4:"Cuatro", 5:"Cinco",
            6:"Seis", 7:"Siete", 8:"Ocho", 9:"Nueve", 10:"Diez",
            11:"Once", 12:"Doce", 13:"Trece", 14:"Catorce", 15:"Quince",
            16:"Dieciséis", 17:"Diecisiete", 18:"Dieciocho", 19:"Diecinueve",
            20:"Veinte", 21:"Veintiuno", 22:"Veintidós", 23:"Veintitrés",
            24:"Veinticuatro", 25:"Veinticinco", 26:"Veintiseis", 27:"Veintisiete",
            28:"Veintiocho", 29:"Veintinueve", 30:"Treinta", 31:"Treinta y uno"
        }

        meses = {
            1:"Enero", 2:"Febrero", 3:"Marzo", 4:"Abril", 5:"Mayo", 6:"Junio",
            7:"Julio", 8:"Agosto", 9:"Septiembre", 10:"Octubre", 11:"Noviembre", 12:"Diciembre"
        }

        @staticmethod
        def getFechaString(fecha):
            # convertir string a un dato tipo datetime
            
            fecha_dt = datetime.strptime(fecha, "%d/%m/%Y")
            dia = FuncionesPrograma.dias[fecha_dt.day]
            mes = FuncionesPrograma.meses[fecha_dt.month]
            anio = fecha_dt.year

            anio_literal = str(anio)  # (versión simple, ej. "1900")
            return f"{dia} de {mes} de {anio_literal}"


    fecha = "15/10/1900"
    print(FuncionesPrograma.getFechaString(fecha))

def ejercicio_18():
    from datetime import datetime, date

    class FuncionesPrograma:
        dias = {
            1:"Uno", 2:"Dos", 3:"Tres", 4:"Cuatro", 5:"Cinco",
            6:"Seis", 7:"Siete", 8:"Ocho", 9:"Nueve", 10:"Diez",
            11:"Once", 12:"Doce", 13:"Trece", 14:"Catorce", 15:"Quince",
            16:"Dieciséis", 17:"Diecisiete", 18:"Dieciocho", 19:"Diecinueve",
            20:"Veinte", 21:"Veintiuno", 22:"Veintidós", 23:"Veintitrés",
            24:"Veinticuatro", 25:"Veinticinco", 26:"Veintiséis", 27:"Veintisiete",
            28:"Veintiocho", 29:"Veintinueve", 30:"Treinta", 31:"Treinta y uno"
        }

        meses = {
            1:"Enero", 2:"Febrero", 3:"Marzo", 4:"Abril", 5:"Mayo", 6:"Junio",
            7:"Julio", 8:"Agosto", 9:"Septiembre", 10:"Octubre", 11:"Noviembre", 12:"Diciembre"
        }

        @staticmethod
        def getFechaString(fecha):
            fecha_dt = datetime.strptime(fecha, "%d/%m/%Y")
            dia = FuncionesPrograma.dias[fecha_dt.day]
            mes = FuncionesPrograma.meses[fecha_dt.month]
            anio_literal = str(fecha_dt.year)
            return f"{dia} de {mes} de {anio_literal}"

        @staticmethod
        def getFechaDate(dia, mes, anio):
            return date(anio, mes, dia)


    fecha_texto = FuncionesPrograma.getFechaString("15/10/1900")
    print("Fecha en cadena:", fecha_texto)

    fecha_date = FuncionesPrograma.getFechaDate(15, 10, 1900)
    print("Fecha como objeto date:", fecha_date)

def ejercicio_19():
    class Operacion_matematicas:
        def __init__(self,valor1,valor2):
            self.valor1=valor1
            self.valor2=valor2

        
        def sumarNumeros(self):
            suma= self.valor1+self.valor2
            print(f"La suma de {self.valor1} y {self.valor2} es {suma}")
        
        
        def restarNumeros(self):
            resta= self.valor1-self.valor2
            print(f"La resta de {self.valor1} y {self.valor2} es {resta}")
            
        def multiplicarNumeros(self):
            multiplicacion= self.valor1*self.valor2
            print(f"La multiplicacion de {self.valor1} y {self.valor2} es {multiplicacion}")

        def dividirNumeros(self):
            division= self.valor1/self.valor2
            print(f"La division de {self.valor1} y {self.valor2} es {division}")

        def aplicarOperaciones(self, operacion):
            if operacion=="+":
                self.sumarNumeros()
            elif operacion=="-":
                self.restarNumeros()
            elif operacion=="*":
                self.multiplicarNumeros()
            elif operacion=="/":
                self.dividirNumeros()
            
    class Calculo: 
        def main(self):
            operacion = Operacion_matematicas(10,5)
            operacion.aplicarOperaciones("+")
            operacion.aplicarOperaciones("-")
            operacion.aplicarOperaciones("*")
            operacion.aplicarOperaciones("/")

    menu = Calculo()
    menu.main()

def ejercicio_20():
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
            num1 = int(input("Ingrese el numerador para la fraccion (1) "))
            num2 = int(input("Ingrese el denominador para la fraccion (1) "))
            num3 = int(input("Ingrese el numerador para la fraccion (2) "))
            num4 = int(input("Ingrese el denominador para la fraccion (2) "))
            
            Fraccion1 = Fraccion(num1,num2)
            Fraccion2 = Fraccion(num3,num4)
            
            ResultadoSuma = Fraccion.SumarFracciones(Fraccion1, Fraccion2) 
            ResultadoResta = Fraccion.RestaFracciones(Fraccion1,Fraccion2)
            ResultadoMultiplicacion = Fraccion.MultiplicacionFracciones(Fraccion1,Fraccion2)
            ResultadoDivision = Fraccion.DivisionFracciones(Fraccion1,Fraccion2)
            print("RESULTADO SUMA DE FRACCION", ResultadoSuma.numerador, "/", ResultadoSuma.denominador)
            print("RESULTADO RESTA DE FRACCION", ResultadoResta.numerador, "/", ResultadoResta.denominador)
            print("RESULTADO MULTIPLICACION DE FRACCION", ResultadoMultiplicacion.numerador, "/", ResultadoMultiplicacion.denominador)
            print("RESULTADO DIVISION DE FRACCION", ResultadoDivision.numerador, "/", ResultadoDivision.denominador)

    OperacionesFracciones.main()

def ejercicio_21():
    #En clase nos pidio que repitamos el ejercicio 20 pero usando metodos de instancia
    
    class Fraccion:
        def __init__(self, numerador,denominador):
            self.numerador = numerador
            self.denominador = denominador

        def SumarFracciones(self, f2):
            numerador = self.numerador * f2.denominador + f2.numerador * self.denominador
            denominador = self.denominador * f2.denominador
            return Fraccion(numerador, denominador)

        def RestaFracciones(self, f2):
            numerador = self.numerador * f2.denominador - f2.numerador * self.denominador
            denominador = self.denominador * f2.denominador
            return Fraccion(numerador, denominador)

        def MultiplicacionFracciones(self, f2):
            numerador = self.numerador * f2.numerador
            denominador = self.denominador * f2.denominador
            return Fraccion(numerador, denominador)


        def DivisionFracciones(self, f2):
            numerador = self.numerador * f2.denominador
            denominador = self.denominador * f2.numerador
            return Fraccion(numerador, denominador)
        
    class OperacionesFracciones:
        def main():
            num1 = int(input("Ingrese el numerador para la fraccion (1) "))
            num2 = int(input("Ingrese el denominador para la fraccion (1) "))
            num3 = int(input("Ingrese el numerador para la fraccion (2) "))
            num4 = int(input("Ingrese el denominador para la fraccion (2) "))
            
            Fraccion1 = Fraccion(num1,num2)
            Fraccion2 = Fraccion(num3,num4)
            
            ResultadoSuma = Fraccion1.SumarFracciones(Fraccion2) 
            ResultadoResta = Fraccion1.RestaFracciones(Fraccion2)
            ResultadoMultiplicacion = Fraccion1.MultiplicacionFracciones(Fraccion2)
            ResultadoDivision = Fraccion1.DivisionFracciones(Fraccion2)
            print("RESULTADO SUMA DE FRACCION", ResultadoSuma.numerador, "/", ResultadoSuma.denominador)
            print("RESULTADO RESTA DE FRACCION", ResultadoResta.numerador, "/", ResultadoResta.denominador)
            print("RESULTADO MULTIPLICACION DE FRACCION", ResultadoMultiplicacion.numerador, "/", ResultadoMultiplicacion.denominador)
            print("RESULTADO DIVISION DE FRACCION", ResultadoDivision.numerador, "/", ResultadoDivision.denominador)

    OperacionesFracciones.main()
    
def menu():
    terminar_ejecucion = False
    while not terminar_ejecucion:
        ejercicio_elegido = int(input("Ingrese el ejercicio que quiere ejecutar [1-21] (0 para terminar): "))
        while not 21>=ejercicio_elegido>=0:
            print("ERROR: Elija un ejercicio entre 1 y 21 ó [0] para terminar la ejecucion")
            ejercicio_elegido = int(input("Ingrese el ejercicio que quiere ejecutar [1-21] (0 para terminar): "))

        if ejercicio_elegido == 0: terminar_ejecucion = True
        elif ejercicio_elegido == 1: ejercicio_1()
        elif ejercicio_elegido == 2: ejercicio_2()
        elif ejercicio_elegido == 3: ejercicio_3()
        elif ejercicio_elegido == 4: ejercicio_4()
        elif ejercicio_elegido == 5: ejercicio_5()
        elif ejercicio_elegido == 6: ejercicio_6()
        elif ejercicio_elegido == 7: ejercicio_7()
        elif ejercicio_elegido == 8: ejercicio_8()
        elif ejercicio_elegido == 9: ejercicio_9()
        elif ejercicio_elegido == 10: ejercicio_10()
        elif ejercicio_elegido == 11: ejercicio_11()
        elif ejercicio_elegido == 12: ejercicio_12()
        elif ejercicio_elegido == 13: ejercicio_13()
        elif ejercicio_elegido == 14: ejercicio_14()
        elif ejercicio_elegido == 15: ejercicio_15 ()
        elif ejercicio_elegido == 16: ejercicio_16()
        elif ejercicio_elegido == 17: ejercicio_17()
        elif ejercicio_elegido == 18: ejercicio_18()
        elif ejercicio_elegido == 19: ejercicio_19()
        elif ejercicio_elegido == 20: ejercicio_20()
        elif ejercicio_elegido == 21: ejercicio_21()

#main
menu()