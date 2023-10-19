fruta = {"Plátano" : 1.35, "Manzana" : 0.80, "Pera" : 0.85, "Naranja" : 0.70}
venta = str(input("Que le gustaría comprar? "))

if venta in fruta:
    kilos = int(input("Cuámtos kilos? "))
    precio = fruta.get(venta) * kilos
    print("Serán", precio, "euros.")
else:
    print("Lo sentimos, no tenemos esa fruta.")