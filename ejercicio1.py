monedas = {"Euros": "€", "Dollar": "$", "Yen": "Y"}
divisa = str(input("Quiere usar Euros, Dollar o Yen? "))
if (divisa in monedas):
    print("Ha seleccionado", divisa, "o", monedas[divisa], "como método de pago.")
else:
    print("Lo sentimos, no usamos esa divisa.")