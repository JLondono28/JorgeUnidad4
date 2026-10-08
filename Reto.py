#Aeronaves = [
#    "Avion 1" = [
#        "Datos" = {
#            "Matrícula: ": "",
#            "Modelo: ": "",
#            "Horas de vuelo acumuladas: ": ""
#        },
#        "Horas acumuladas de componentes" = {
#            "Motor izquierdo: ": "",
#            "Motor derecho: ": "",
#            "Tren de aterrizaje: ": "",
#            "Rudder: ": "",
#            "Líquido hidráulico: ": ""
#        }
#    ]
#    ,
#    "Avion 2" = [
#        "Datos" = {
#            "Matrícula: ": "",
#            "Modelo: ": "",
#            "Horas de vuelo acumuladas: ": ""
#        },
#        "Horas acumuladas de componentes" = {
#            "Motor izquierdo: ": "",
#            "Motor derecho: ": "",
#            "Tren de aterrizaje: ": "",
#            "Rudder: ": "",
#            "Líquido hidráulico: ": ""
#        }
#    ]
#    ,
#    "Avion 3" = [
#        "Datos" = {
#            "Matrícula: ": "",
#            "Modelo: ": "",
#            "Horas de vuelo acumuladas: ": ""
#        },
#        "Horas acumuladas de componentes" = {
#            "Motor izquierdo: ": "",
#            "Motor derecho: ": "",
#            "Tren de aterrizaje: ": "",
#            "Rudder: ": "",
#            "Líquido hidráulico: ": ""
#        }
#    ]
#]

Datos1 = {
    "Matrícula: ": "HK-4532",
    "Modelo: ": "B737",
    "Horas de vuelo acumuladas: ": 0
}
Horas_ac1 = {
            "Motor izquierdo: ": 0,
            "Motor derecho: ": 0,
            "Tren de aterrizaje: ": 0,
            "Rudder: ": 0,
            "Líquido hidráulico: ": 0
}
Horas_max1 = {
            "Motor izquierdo: ": 1000,
            "Motor derecho: ": 1000,
            "Tren de aterrizaje: ": 800,
            "Rudder: ": 2000,
            "Líquido hidráulico: ": 800
}
Datos2 = {
    "Matrícula: ": "HJ-7483",
    "Modelo: ": "A320",
    "Horas de vuelo acumuladas: ": 0
}
Horas_ac2 = {
            "Motor izquierdo: ": 0,
            "Motor derecho: ": 0,
            "Tren de aterrizaje: ": 0,
            "Rudder: ": 0,
            "Líquido hidráulico: ": 0
}
Horas_max2 = {
            "Motor izquierdo: ": 1500,
            "Motor derecho: ": 1500,
            "Tren de aterrizaje: ": 700,
            "Rudder: ": 2500,
            "Líquido hidráulico: ": 700
}
Datos3 = {
    "Matrícula: ": "MN-1011",
    "Modelo: ": "ATR72",
    "Horas de vuelo acumuladas: ": 0
}
Horas_ac3 = {
            "Motor izquierdo: ": 0,
            "Motor derecho: ": 0,
            "Tren de aterrizaje: ": 0,
            "Rudder: ": 0,
            "Líquido hidráulico: ": 0
}
Horas_max3 = {
            "Motor izquierdo: ": 1200,
            "Motor derecho: ": 1200,
            "Tren de aterrizaje: ": 500,
            "Rudder: ": 1500,
            "Líquido hidráulico: ": 500
}


Avion1 = [Datos1, Horas_ac1, Horas_max1]
Avion2 = [Datos2, Horas_ac2, Horas_max2]
Avion3 = [Datos3, Horas_ac3, Horas_max3]

Aeronaves = [Avion1, Avion2, Avion3]

while True:
    print("---- BIENVENIDOS ----")
    print("Seleccione una opción: ")
    print("1. Ingresar nueva aeronave")
    print("2. Agregar componentes a una aeronave")
    print("3. Registrar horas de vuelo")
    print("4. Revisar horas de vuelo y mantenimiento")
    print("5. Mostrar todas las aeronaves y sus componentes")
    print("6. Salir")
    opcion = input("Ingrese una opción (1-6): ")

    if opcion == "1":
        print("---- Ingresar nueva aeronave ----")
        matricula = input("Ingrese la matrícula de la aeronave: ").upper()
        if matricula in [avion[0]["Matrícula: "] for avion in Aeronaves]:
            print("La matrícula ya existe. No se puede ingresar la aeronave.")
        else:
            modelo = input("Ingrese el modelo de la aeronave: ")
            horas_vuelo = 0
            Datos_nueva = {
                "Matrícula: ": matricula,
                "Modelo: ": modelo,
                "Horas de vuelo acumuladas: ": horas_vuelo
            }
            Horas_ac_nueva = {
                "Motor izquierdo: ": 0,
                "Motor derecho: ": 0,
                "Tren de aterrizaje: ": 0,
                "Rudder: ": 0,
                "Líquido hidráulico: ": 0
            }
            Horas_max_nueva = {
                "Motor izquierdo: ": 1000,
                "Motor derecho: ": 1000,
                "Tren de aterrizaje: ": 800,
                "Rudder: ": 2000,
                "Líquido hidráulico: ": 800
            }
            Avion_nuevo = [Datos_nueva, Horas_ac_nueva, Horas_max_nueva]
            Aeronaves.append(Avion_nuevo)
            print("Aeronave ingresada exitosamente.")
    elif opcion == "2":
        print("---- Agregar componentes a una aeronave ----")
        matricula = input("Ingrese la matrícula de la aeronave: ").upper()
        if matricula in [avion[0]["Matrícula: "] for avion in Aeronaves]:
            for avion in Aeronaves:
                if avion[0]["Matrícula: "] == matricula:
                    pieza = input("Ingrese el nombre del componente: ")
                    limite = int(input("Ingrese el límite de horas del componente: "))
                    avion[1][pieza] = 0
                    avion[2][pieza] = limite
                    print(f"Componente agregado a la aeronave {matricula} exitosamente.")
                    break
        else:
                print("Aeronave no encontrada.")
    elif opcion == "3":
        print("---- Registrar horas de vuelo ----")
        print(f"Aeronaves: {[avion[0]['Matrícula: '] for avion in Aeronaves]}")
        matricula = input("Ingrese la matrícula de la aeronave: ").upper()
        if matricula in [avion[0]["Matrícula: "] for avion in Aeronaves]:
            horas_vuelo = int(input("Ingrese las horas de vuelo: "))
            for avion in Aeronaves:
                if avion[0]["Matrícula: "] == matricula:
                    avion[0]["Horas de vuelo acumuladas: "] += horas_vuelo
                    for componente in avion[1]:
                        avion[1][componente] += horas_vuelo
                    print("Horas de vuelo registradas exitosamente.")
                    for componente, horas in avion[1].items():
                        if horas >= avion[2][componente]:
                            print(f"El componente {componente} ha alcanzado su límite de horas. Se requiere mantenimiento.")
        else:
            print("Aeronave no encontrada.")                
    elif opcion == "4":
        print("---- Revisar horas de vuelo y mantenimiento ----")
        print(f"Aeronaves: {[avion[0]['Matrícula: '] for avion in Aeronaves]}")
        matricula = input("Ingrese la matrícula de la aeronave: ").upper()
        if matricula in [avion[0]["Matrícula: "] for avion in Aeronaves]:
            for avion in Aeronaves:
                if avion[0]["Matrícula: "] == matricula:
                    print(f"Matrícula: {avion[0]['Matrícula: ']}")
                    print(f"Modelo: {avion[0]['Modelo: ']}")
                    print(f"Horas de vuelo acumuladas: {avion[0]['Horas de vuelo acumuladas: ']}")
                    print("Horas acumuladas de componentes:")
                    for componente, horas in avion[1].items():
                        print(f"{componente} {horas} / {avion[2][componente]} horas")
                        if horas >= avion[2][componente]:
                            print(f"El componente {componente} ha alcanzado su límite de horas. Se requiere mantenimiento.")
                            realizar_mantenimiento = input(f"¿Desea realizar mantenimiento del componente {componente}? (si/no): ")
                            if realizar_mantenimiento.lower() == "si":
                                avion[1][componente] = 0
                                print(f"Mantenimiento del componente {componente} realizado exitosamente.")
                    break
        else:
            print("Aeronave no encontrada.")
    elif opcion == "5":
        print("---- Ver todas las aeronaves y sus componentes ----")
        for avion in Aeronaves:
            print(f"Matrícula: {avion[0]['Matrícula: ']}")
            print(f"Modelo: {avion[0]['Modelo: ']}")
            print(f"Horas de vuelo acumuladas: {avion[0]['Horas de vuelo acumuladas: ']}")
            print("Horas acumuladas de componentes:")
            for componente, horas in avion[1].items():
                print(f"{componente} {horas} / {avion[2][componente]} horas")
                if horas >= avion[2][componente]:
                    print(f"El componente {componente} ha alcanzado su límite de horas. Se requiere mantenimiento.")        
    elif opcion == "6":
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida (1-6).")
