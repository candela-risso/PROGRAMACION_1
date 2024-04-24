#import os
from funciones import *

def menu():
    bandera_operando1=False
    bandera_operando2=False
    while(True):

        print("MENU CALCULADORA\n1.Ingresar Primer Operando\n2.Ingresar Segundo Operando\n3.Calcular Todas las operaciones\n4.Informar Resultados\n5.Salir")
    
        opcion= input("Su opcion:")
        while not opcion.isdigit() or opcion is None:
            opcion = (input("Ingrese de nuevo su opcion: "))
        opcion= int(opcion)
        
        if opcion ==1:
            print("Ingrese un numero entero")
            operando1 = (input())
            while operando1 is None or not operando1.isdigit():
                operando1 = (input("ingrese nuevamente el primer operando\t"))
            operando1 = int(operando1)
            bandera_operando1=True

        elif opcion ==2:
            print("Ingreso un segundo numero entero")
            operando2 = (input())
            while operando2 is None or not operando2.isdigit():
                operando2 = (input("ingrese nuevamente el segundo operando\t"))
            operando2 = int(operando2)
            bandera_operando2=True
        
        elif opcion ==3:
            if bandera_operando2==True and bandera_operando1==True:
                print("Calculo todas las operaciones")
                suma=sumar(operando1,operando2)            
                resta=restar(operando1,operando2)           
                multiplicacion=multiplicar(operando1,operando2)            
                division=dividir(operando1,operando2)            
                potencia=calcular_potencia(operando1,operando2)            
                resto=calcular_resto(operando1,operando2)           
                factorial_operando1= calcular_factorial(operando1)
                factorial_operando2= calcular_factorial(operando2)
            else:
                print("Antes de calcular registre ambos valores en las opciones 1 y 2")

            
        elif opcion ==4:
            if bandera_operando2==True and bandera_operando1==True:
                print("Informo todos los resultados\n")
                print("La suma entre {0} y {1} es igual a:{2}\n".format(operando1,operando2,suma))
                print("La resta entre {0} y {1} es igual a:{2}\n".format(operando1,operando2,resta))
                print("La multiplicacion entre {0} y {1} es igual a:{2}\n".format(operando1,operando2,multiplicacion))
                print("La division entre {0} y {1} es igual a:{2}\n".format(operando1,operando2,division))
                print("La potencia entre {0} y {1} es igual a:{2}\n".format(operando1,operando2,potencia))
                print("El resto entre {0} y {1} es igual a:{2}\n".format(operando1,operando2,resto))
                print("El factorial de {0} es igual a:{1}\n".format(operando1,factorial_operando1))
                print("El factorial de {0} es igual a:{1}\n".format(operando2,factorial_operando2))
            else:
                print("Antes de calcular registre ambos valores en las opciones 1 y 2")

        elif opcion ==5:
            print("Saliendo...")
            break
        else:
            print("Opcion invalida ingrese números entre 1-5")
            
        #os.system('clear')
    
    
menu()
