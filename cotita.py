#Ejercicio 16

def contiene_num(cadena): 
    resultado= False
    for i in cadena:
        if i.isnumeric() == True: resultado= True
    if resultado == True: print("contiene numeros")
    else: print ("no contiene numeros")
contiene_num("hola2")

#Ejercicio 18/17(anda  saber si esta bien abrazos y bendiciones)
#FuncionesPrograma.py

from datetime import date

class FuncionesPrograma:
    @staticmethod
    def getFechaDate(dia, mes, anio):
        return date(anio, mes, dia)

#Principal.py
from FuncionesPrograma import FuncionesPrograma

def main():
    fecha = FuncionesPrograma.getFechaDate(15, 10, 1900)
    print("La fecha es:", fecha)

if __name__ == "__main__":
    main()

