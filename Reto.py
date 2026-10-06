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

(Aeronaves[0][1]["Motor izquierdo: "]) = input("Ingrese las horas de vuelo del motor izquierdo: ")

print(f"{Aeronaves[0][1]["Motor izquierdo: "]}")