"""""""""
Debemos realizar la carga de 5 (cinco) productos de prevención de
contagio, de cada una debe obtener los siguientes datos:
1. El tipo (validar "barbijo", "jabón" o "alcohol")
2. El precio: (validar entre 100 y 300)
3. La cantidad de unidades ( no puede ser 0 ni negativo y no debe superar las
1000 unidades)
4. La marca y el Fabricante.
Se debe informar lo siguiente:
A. Del más caro de los barbijos, la cantidad de unidades y el fabricante.
B. Del ítem con más unidades, el fabricante.
C. Cuántas unidades de jabones hay en total.
"""""""""

tipo = ""
precio=0
cantidad=0
marca=""
fabricante=""
acumulador_jabon=0
mayor_cantidad=0
mayor_cantidad_fabricante=""
item_mayor_cantidad=""
barbijo_mas_caro=0
barbijo_mas_caro_cantidad=0
barbijo_mas_caro_fabricante=""

for i in range(5):

    tipo=input("Ingrese tipo del {}° objeto a registrar".format(i+1))
    while tipo.lower() != "barbijo" and tipo.lower() != "jabon" and tipo.lower() != "alcohol":
        tipo=input("Ingrese nuevamente tipo del {}° objeto a registrar".format(i+1))
    tipo=tipo.lower()
    
    precio=input("Ingrese precio del {}° objeto a registrar".format(i+1))
    while precio is None or precio=="" or not precio.isdigit() or int(precio) < 100 or int(precio) > 300:
        precio=input("Ingrese nuevamente precio del {}° objeto a registrar".format(i+1))
    precio=int(precio)

    cantidad=input("Ingrese cantidad de unidades del {}° objeto a registrar".format(i+1))
    while cantidad is None or cantidad=="" or not cantidad.isdigit() or int(cantidad) < 0 or int(cantidad) > 1000:
        cantidad=input("Ingrese nuevamente cantidad de unidades del {}° objeto a registrar".format(i+1))
    cantidad=int(cantidad)

    marca=input("Ingrese marca del {}° objeto a registrar".format(i+1))
    while marca is None or marca=="":
        marca=input("Ingrese nuevamente marca del {}° objeto a registrar".format(i+1))
    
    fabricante=input("Ingrese fabricante del {}° objeto a registrar".format(i+1))
    while fabricante is None or fabricante=="":
        fabricante=input("Ingrese nuevamente fabricante del {}° objeto a registrar".format(i+1))
    
    match tipo:
        case "barbijo":
            if i==0 or precio>barbijo_mas_caro:
                barbijo_mas_caro=precio
                barbijo_mas_caro_fabricante=fabricante
                barbijo_mas_caro_cantidad=cantidad
        
        case "jabon":
            acumulador_jabon += 1
        
    
    if i==0 or cantidad>mayor_cantidad:
        mayor_cantidad=cantidad
        mayor_cantidad_fabricante=fabricante
        item_mayor_cantidad=tipo

print("La cantidad de barbijos mas caros es: {} y los fabrica: {}".format(barbijo_mas_caro_cantidad, barbijo_mas_caro_fabricante))
print("El item con mas unidades es: {} y los fabrica: {}".format(item_mayor_cantidad,mayor_cantidad_fabricante))
print("El total de jabones es: {}".format(acumulador_jabon))