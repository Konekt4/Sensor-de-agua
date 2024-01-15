#Katana

import json
import os

ruta = os.getcwd()
contenido = os.listdir(ruta)
funcionamiento = []

for archivo in contenido:
    if os.path.isfile(os.path.join(ruta, archivo)) and archivo.endswith('.json'):
        funcionamiento.append(archivo)

# preingreso

A = {}

A['registro'] = []

A['ajustes'] = [{"alerta" : "60"}]

if "Registro_de_agua.json" not in funcionamiento:
    with open("Registro_de_agua.json", "w") as file:
        json.dump(A, file, indent=4)

salir = 0

#ajustes_de_usuario
while salir == 0:
    with open('Registro_de_agua.json') as file:
            ingreso = json.load(file)

    for i in ingreso['ajustes']:
        ajuste = str(input("Ingrese la cantidad de segundos para mostrar una alerta en caso de flujo anormal de agua: "))
        i['alerta'] = ajuste

    with open('Registro_de_agua.json','w') as file:
        json.dump(ingreso,file,indent=4)
    
    while True:
        entrada = str(input("¿Desea salir del programa?: "))

        if entrada == "1" or entrada == "si" or entrada == "Si" or entrada == "sI":
            salir = 1
            break
        elif entrada == "0" or entrada == "no" or entrada == "No" or entrada == "nO":
            break
        else:
            continue
