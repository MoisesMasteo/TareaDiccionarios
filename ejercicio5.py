creditos = {"Mates" : 6, "Fisica" : 4, "Quimica" : 5}
creditos_totales = creditos.get("Mates") + creditos.get("Fisica") + creditos.get("Quimica")

for asignaturas, creditos in creditos.items():
    print(f"{asignaturas} tiene {creditos} créditos.")

print("En total el curso tiene", creditos_totales, "créditos.")