diccionario = {}

preg = input("Dime una palabra en (español:traducción) en ingles la tradicción: ")
sep = preg.split(":")

diccionario[f"{sep[0]}"] = sep[1]

preg_2 = input("Dime una palabra que quieras traduccir: ")
if preg_2 not in diccionario:
    print ("Esa palabra no la tenemos en la base de datos.")
else:
    print("La traducción de", preg_2, "es", diccionario[f"{preg_2}"])