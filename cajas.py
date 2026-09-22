def cargar_cajas(pesos, peso_maximo):
    """
    Selecciona cajas para cargar en la aeronave sin exceder el peso máximo.

    Args:
        pesos: lista de pesos de las cajas (kg)
        peso_maximo: peso máximo permitido (kg)
    """
    # Tu código aquí
    indices_cajas = []
    if not pesos:
        return None
    
    suma = 0
    for i in range(len(pesos)):
        indices_cajas.append(i)
        suma += pesos[i]
        if suma > peso_maximo:
            suma -= pesos[i]
            indices_cajas.pop()
            break
        elif suma == peso_maximo:
            break
    return indices_cajas

# Datos de prueba
pesos_cajas = [120, 400, 300, 180, 450, 200]
peso_max_avion = 1000

cajas = cargar_cajas(pesos_cajas, peso_max_avion)

if not cajas:
    print("No hay cajas")
elif cajas != None:
    print(f"Las cajas que se pueden subir son: {cajas}")
else:
    print("Revise los datos enviados")
