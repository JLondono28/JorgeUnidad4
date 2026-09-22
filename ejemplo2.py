from random import randint

meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
ventas = []

for i in range(12):
    ventas.append(randint(200,3000))
    print(f"{meses[i]} - ${ventas[i]}")

prom_ventas = sum(ventas) / 12
mayor = max(ventas)
pos = ventas.index(mayor)
menor = min(ventas)
pes = ventas.index(menor)

print(f"Mayor venta fue de ${menor} en el mes {meses[pes]}")
print(f"Mayor venta fue de ${mayor} en el mes {meses[pos]}")
print(ventas)
print(prom_ventas)
