from random import randint, uniform

lista = []
impares = []
pares = []

dato = randint(0,100)
lista.append(dato)

for i in range(10):
    dato = randint(0,100)
    lista.append(dato)
print(lista)

for dato in lista:
    if dato % 2 == 0:
        pares.append(dato)
    else:
        impares.append(dato)

print(f"Pares: {pares}")
print(f"Impares: {impares}")

#Calcular el promedio de lista, pares e impares
suma = 0
for dato in lista:
    suma += dato
prom_lista = suma / len(lista)
for dato in pares:
    suma += dato
prom_pares = suma / len(pares)
for dato in impares:
    suma += dato
prom_impares = suma / len(impares)

print(f"Promedio de lista: {prom_lista}")
print(f"Promedio de números pares: {prom_pares}")
print(f"Promedio de números impares: {prom_impares}")