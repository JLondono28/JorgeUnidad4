import random

aviones = ["A320", "B747", "CESSNA-172", "A380", "STOL701"]
lista_vacia = []

if aviones: 
    print("Esta lista contiene elementos")

if not lista_vacia:
    print("Esta lista está vacía")
else:
    print("La lista contiene elementos")

modelo = input("Ingrese el modelo: ")

if modelo in aviones:
    print("El avión pertenece a mi colección privada")
else:
    print("El avión no pertenece a mi colección privada")

#Elegir un elemento de la lista al azar
avion = random.choice(aviones)
print(avion)