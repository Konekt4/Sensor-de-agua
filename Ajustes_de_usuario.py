#Katana

#Se crea un archivo tipo Json para hacer el registro del flujo de agua y más
import json
import os

#Variables para obtener la ruta donde se generará el archivo Json
ruta = os.getcwd()
contenido = os.listdir(ruta)
funcionamiento = []

#Ciclo for para buscar el archivo Json
for archivo in contenido:
    #Si el archivo Json ya existía en este punto lo almacena en una lista llamada "Funcionamiento"
    if os.path.isfile(os.path.join(ruta, archivo)) and archivo.endswith('.json'):
        funcionamiento.append(archivo)

# Preingreso de datos al archivo Json
#1
A = {}

A['registro'] = []

A['ajustes'] = [{"alerta" : "60"}]

#Si no se encontró el archivo Json, lo crea automáticamente
if "Registro_de_agua.json" not in funcionamiento:
    with open("Registro_de_agua.json", "w") as file:
        json.dump(A, file, indent=4)

#Variable que  incida si el usuario ha decidio salir de los ajustes o no
salir = 0

#Programa que permite cambiar cuándo mandar alertas en Sensor_de_agua.py
while salir == 0:
    #Se prepara el archivo Json para guardar la alerta
    with open('Registro_de_agua.json') as file:
            ingreso = json.load(file)

    #Se utiliza la variable ingreso para con un for obtener la variable ajuste que determina la alerta
    for i in ingreso['ajustes']:
        ajuste = str(input("Ingrese la cantidad de segundos para mostrar una alerta en caso de flujo anormal de agua: "))
        i['alerta'] = ajuste

    #Se guarda la alerta en el archivo Json
    with open('Registro_de_agua.json','w') as file:
        json.dump(ingreso,file,indent=4)
    
    #Ciclo While que pregunta si el usuario desea salir del programa
    while True:
        entrada = str(input("¿Desea salir del programa?: "))

        if entrada == "1" or entrada == "si" or entrada == "Si" or entrada == "sI":
            salir = 1
            break
        elif entrada == "0" or entrada == "no" or entrada == "No" or entrada == "nO":
            break
        else:
            continue
