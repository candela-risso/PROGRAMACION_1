numero=None
def sumar_naturales(numero:int)->int:
    """
    suma los números naturales desde 1 hasta el número ingresado por parámetro
    :param numero: int
    :return: int
    """
    if  numero==0:
        resultado= 0
    else:
        resultado= numero + sumar_naturales(numero-1)
    return resultado

#numero=int(input("ingrese un numero entero positivo"))
#resultado= print(sumar_naturales(numero))

def calcular_potencia(base,exponente):
    if exponente==0:
        resultado= 1
    elif exponente>0:
        resultado= base*calcular_potencia(base,exponente-1)
    else:
        resultado=base*calcular_potencia(base,exponente+1)
        resultado=1/resultado
    return resultado

#base=int(input("ingrese un numero entero"))
#exponente=int(input("ingrese un numero entero"))
#resultado=print(calcular_potencia(base, exponente))

def sumar_digitos(numero:int)->int:
    """
    suma los dígitos de un número ingresado por parámetro
    :param numero: int
    :return: int
    """
    if numero == 0:
        resultado = 0
    else:
        resultado = numero % 10 + sumar_digitos(numero // 10)
    return resultado

#numero=int(input("ingrese un numero entero positivo"))
#resultado=print(sumar_digitos(numero))

def calcular_fibonacci(numero:int)->int:
    """
    calcula el n-ésimo número de la sucesión de Fibonacci
    :param numero: int
    :return: int
    """
    if numero==0:
        resultado=0
    elif numero==1:
        resultado=1
    else:
        resultado=calcular_fibonacci(numero-1)+calcular_fibonacci(numero-2)
    return resultado

#numero=int(input("ingrese un numero entero positivo"))
#resultado=print(calcular_fibonacci(numero))