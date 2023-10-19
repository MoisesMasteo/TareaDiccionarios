mes = {"1" : "enero", "2" : "febrero", "3" : "marzo", "4" : "abril", "5" : "mayo", "6" : "junio",
 "7" : "julio", "8" : "agosto", "9" : "septiembre", "10" : "octubre", "11" : "noviembre", "12" : "diciembre"}

fecha_us = input("A que fecha estamos usando dd/mm/aa? ")
separa = fecha_us.split("/")

fecha = {}
fecha["dia"]=separa[0]
fecha["mes"]=separa[1]
fecha["año"]=separa[2]

print(fecha)
#print(fecha.get("dia"), "de", mes.get(fecha.get("mes")), "de", fecha.get("año"))