
def sumar(operando1:int, operando2:int):
    return operando1 + operando2

def restar(operando1:int, operando2:int):
    return operando1 - operando2

def multiplicar(operando1:int, operando2:int):
    return operando1 * operando2

def dividir(operando1:int, operando2:int):
    return operando1 / operando2

def calcular_potencia(operando1:int, operando2:int):
    return operando1 ** operando2

def calcular_resto(operando1:int, operando2:int):
    return operando1 % operando2

def calcular_factorial(numero:int):
    for i in range(1,numero+1):
        if i==1:
            factorial = 1
        factorial *= i
    return factorial
