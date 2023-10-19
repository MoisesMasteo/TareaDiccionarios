cesta = {}
while True:
    compra = str(input("Que quieres comprar? "))
    coste = int(input("Cuanto cuesta? "))

    cesta[compra] = coste
    print("La cesta actual es: ")
    for compra, coste in cesta.items():
        print(f"{compra}: {coste}")

    seguir = input("Quieres seguir comprando? ").lower()
    if seguir != "si":
        print("La cesta final es: ")
        for compra, coste in cesta.items():
            print(f"{compra}: {coste}")