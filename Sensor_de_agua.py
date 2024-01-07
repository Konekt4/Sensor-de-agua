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
    from gpiozero import Button, LED
    import json
    import os
    from datetime import datetime
    datetime=datetime.now()
    funcionamiento = []

    json_crear(os, funcionamiento, json)

    pin_flujo_agua = 17
    pin_led = LED(16)

    sensor_flujo = Button(pin_flujo_agua)

    def flujo_agua_detectado():
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
        if sensor_flujo.when_pressed is True:
            flujo_agua_detectado()
            pin_led.on()

        elif sensor_flujo.when_pressed is False:
            pin_led.off()

#Inicio
imprimir()
