from math import *

def ingresar_lado() -> float:
    lado = (input())
    while lado is None or not lado.isdigit() or int(lado) <= 0:
        print("El lado debe ser mayor a 0")
        lado = float(input())
    lado = float(lado)
    return lado

def calcular_area_triangulo(base: float, altura: float):
    area = (base * altura) / 2
    return area

def calcular_area_cuadrado(base: float, altura: float):
    area = base * altura
    return area

def calcular_area_rectangulo(base: float, altura: float):
    area = base * altura
    return area
def calcular_diagonal(base: float, altura: float):
    diagonal= sqrt((base * base) +(altura* altura))
    return diagonal

def calcular_perimetro_triangulo(base: float, altura: float):
    perimetro = base + altura + calcular_diagonal(base, altura)
    return perimetro

def calcular_perimetro_cuadrado(base: float, altura: float):
    perimetro = base * 4
    return perimetro

def calcular_perimetro_rectangulo(base: float, altura: float):
    perimetro = base * 2 + altura * 2
    return perimetro


def calcular_grados_angulos(base:float, altura:float)-> str:
    angulo1= degrees(acos(base / calcular_diagonal(base, altura)))
    angulo2= 90 - angulo1
    mensaje_angulos= "sus angulos son 90 - {0} - {1}".format(angulo1, angulo2)
    return mensaje_angulos


