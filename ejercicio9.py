facturas = {}
cobrar = 0
pend = 0
preg = input("Que quieres hacer? Añadir una factura (nueva), pagar una factura (pay) o terminar la sesión (end): ")
while preg != "end":
    if preg == "nueva":
        clave = input("Numero de la factura? ")
        coste = int(input("Introduce el coste de la factura: "))
        facturas[clave] = coste
        pend += coste
    elif preg == "pay":
        clave = input("Numero de la factura a pagar: ")
        coste = facturas.pop(clave, 0)
        cobrar += coste
        pend -= coste
    print("Dinero cobrado:", cobrar)
    print("Dinero a pagar:", pend)
    if preg == "end":
        print("Gracias por su visita.")    
    preg = input("Que quieres hacer? Añadir una factura (nueva), pagar una factura (pay) o terminar la sesión (end): ")