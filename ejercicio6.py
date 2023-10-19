persona = {}
nombre = str(input("Como te llamas? "))
edad = int(input("Cuantos años tienes? "))
sexo = str(input("Cuál es tu sexo? "))
tel = int(input("Numero de tel: "))
correo = str(input("Correo electrónico: "))

persona["nombre"] = nombre
persona["edad"] = edad
persona["sexo"] = sexo
persona["tel"] = tel
persona["correo"] = correo

print("El contenido del diccionario es: ", persona) #DE ESTA FORMA SOBREESCRIBE LA INFORMACIÓN QUE HABÍA ANTES POR LA NUEVA