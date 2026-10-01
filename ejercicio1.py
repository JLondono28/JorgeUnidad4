diccionario = {
    "Clave1": "Valor1",
    "Clave2": "Valor2",
    "Clave3": "Valor3"
}
print(diccionario)

diccionario.setdefault("Clave4")

print(diccionario)

diccionario["Clave4"] = "Valor4"

print(diccionario)

diccionario.popitem()

print(diccionario)

claves = diccionario.keys()

print(claves)