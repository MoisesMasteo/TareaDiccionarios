diccionario = {"nombre" : "","edad" : "","direccion" : "","tel" : ""}
nombre = str(input("Cuál es tu nombre? "))
edad = int(input("Cuántos años tienes? "))
direccion = str(input("Donde vives? "))
tel = int(input("Cuál es tu numero de telefono? "))

diccionario["nombre"] = nombre
diccionario["edad"] = edad
diccionario["direccion"] = direccion
diccionario["tel"] = tel

print(diccionario["nombre"], "tiene", diccionario["edad"], "años, vive en", diccionario["direccion"], "y su numero de telefono es", diccionario["tel"])