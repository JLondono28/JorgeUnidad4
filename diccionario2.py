vuelo = {
    "aerolinea": "Avianca",
    "vuelo": "AV123",
    "origen": "BOG",
    "destino": "MDE"
}

ciudad_llegada = vuelo["destino"]
print(f"El destino es {ciudad_llegada}")

vuelo["destino"] = "CLO"
print(vuelo)

vuelo["estado"] = "En el aire"
print(vuelo)

piloto = vuelo.get("Piloto", "Piloto no asignado")
print(piloto)

del vuelo["vuelo"]
print(vuelo)