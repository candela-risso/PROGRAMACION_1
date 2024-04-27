from funciones_formas import *
from math import *

base=None
altura=None
bandera_base=False
bandera_altura=False
perimetro=0
area=0
diagonal=0
angulos=""
forma=""
while(True):

    print("1.Ingresar altura de la figura")
    print("2.Ingresar base de la figura")
    print("3.Calcular datos del triangulo rectangulo (Hipotenusa y angulos, area, perimetro)")
    print("4.Calcular datos rectangulo (Diagonal, area, perimetro)")
    print("5.Calcular datos cuadrado (Diagonal, area, perimetro)")
    print("6.Imprimir datos guardados")
    print("7.Borrar datos guardados")
    print("8.Salir")

    opcion = (input("Ingrese una opcion"))
    while not opcion.isdigit() or opcion is None or int(opcion)<1 or int(opcion)>8:
        opcion = (input("Ingrese de nuevo su opcion: "))
    opcion= int(opcion)

    match opcion:
        case 1:
            print("Ingresar altura de la figura")
            altura=ingresar_lado()
            bandera_altura=True

        case 2:
            print("Ingresar base de la figura")
            base=ingresar_lado()
            print(base)
            bandera_base=True

        case 3:
            forma="triangulo"
            if bandera_base==False or bandera_altura==False:
                print("Antes de calcular registre ambos valores en las opciones 1 y 2")
            else:
                print("Calculando datos del triangulo rectangulo (Hipotenusa y angulos, area, perimetro)")
                forma="triangulo"
                print(base)
                print(altura)
                diagonal=calcular_diagonal(base,altura)
                angulos=calcular_grados_angulos(base,altura)#recordar que devuelve str
                area=calcular_area_triangulo(base,altura)
                perimetro=calcular_perimetro_triangulo(base,altura)
        case 4:            
            if bandera_base==False or bandera_altura==False :
                print("Antes de calcular registre ambos valores en las opciones 1 y 2")
            else:
                forma="rectangulo"
                print("Calculando datos rectangulo (Diagonal, area, perimetro)")
                diagonal=calcular_diagonal(base,altura)
                area=calcular_area_rectangulo(base,altura)
                perimetro=calcular_perimetro_rectangulo(base,altura)

        case 5:

            if bandera_base==False or bandera_altura==False:
                print("Antes de calcular registre ambos valores en las opciones 1 y 2")
            else:
                forma="cuadrado"
                print("Calculando datos cuadrado (Diagonal, area, perimetro)")
                diagonal=calcular_diagonal(base,altura)
                area=calcular_area_cuadrado(base,altura)
                perimetro=calcular_perimetro_cuadrado(base,altura)
        case 6:
            match forma:
                case "triangulo":
                    print("El perimetro del triangulo es {0}, su area es {1}, su hipotenusa {2} y {3} grados".format(perimetro, area, diagonal, angulos))
                case _:
                    print("El perimetro de su forma es {0}, su area es {1}, su diagonal {2}".format(perimetro, area, diagonal))
        case 7:
            print("Borrar datos guardados")
            base = None
            altura= None
            bandera_base=False
            bandera_altura=False
            perimetro=0
            area=0
            diagonal=0
            angulos=""
            forma=""

        case 8:
            print("Salir")
            break