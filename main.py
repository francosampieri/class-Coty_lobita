
#Ejercicio 19: #

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

laconchadetumadre = Calculo()
laconchadetumadre.main()
#Ejercicio 4#
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

   
num=leer_numero()
d1,d2,d3=descomponer_numero(num)
suma=sumar_numeros(d1,d2,d3)
print(f"La suma de los digitos del numero {num} es {suma}")