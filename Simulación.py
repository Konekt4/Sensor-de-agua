#Katana

def json_crear(os, funcionamiento, json):

    ruta = os.getcwd()
    contenido = os.listdir(ruta)

    for archivo in contenido:
        if os.path.isfile(os.path.join(ruta, archivo)) and archivo.endswith('.json'):
            funcionamiento.append(archivo)

    # preingreso

    A = {}

    A['fecha'] = []

    if "Sensor_agua.json" not in funcionamiento:
        with open("Sensor_agua.json", "w") as file:
            json.dump(A, file, indent=4)

def imprimir():
    programa()

def programa():
    #from gpiozero import Button, LED
    import json
    import os
    from datetime import datetime
    funcionamiento = []

    json_crear(os, funcionamiento, json)

    #pin_flujo_agua = "Agua"
    pin_led = "Foco"

    def flujo_agua_detectado(datetime):
        z = {}
        with open('Sensor_agua.json') as file:
            salida = json.load(file)

        texto = f"¡Flujo de agua detectado! {datetime}"
        print(texto)
        z['fecha'] = texto
        salida['fecha'].append(z.copy())

        with open('Sensor_agua.json','w') as file:
            json.dump(salida,file,indent=4)
            
    while True:
        sensor_flujo = str(input("Ingrese 1 o 0 ----> "))
        if sensor_flujo == "1":
            datetime=datetime.now()
            flujo_agua_detectado(datetime)
            print(pin_led," prendido")

        elif sensor_flujo == "0":
            print(pin_led," apagado")

#Inicio
imprimir()
