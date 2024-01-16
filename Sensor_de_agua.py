#Katana

def json_crear(os, funcionamiento, json):

    ruta = os.getcwd()
    contenido = os.listdir(ruta)

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

def imprimir():
    programa()

def flujo_agua_detectado(datetime, json):
    z = {}
    with open('Registro_de_agua.json') as file:
        salida = json.load(file)

    texto1 = "Flujo de agua detectado!"
    texto2 = str(datetime)
    print(texto1, texto2)
    z['aviso'] = texto1
    z['fecha'] = texto2
    salida['registro'].append(z.copy())

    with open('Registro_de_agua.json','w') as file:
        json.dump(salida,file,indent=4)
    
def alerta_agua_detecado(datetime, json):
    y = {}
    with open('Registro_de_agua.json') as file:
        salida = json.load(file)

    texto1 = "Alerta!, flujo anormal de agua por tiempo prolongado detectado"
    texto2 = str(datetime)
    print(texto1, texto2)
    y['alerta'] = texto1
    y['fecha'] = texto2
    salida['registro'].append(y.copy())

    with open('Registro_de_agua.json','w') as file:
        json.dump(salida,file,indent=4)

def programa():
    from gpiozero import Button, LED
    import json
    import os
    from datetime import datetime
    funcionamiento = []

    x = 0

    json_crear(os, funcionamiento, json)

    pin_flujo_agua = 17
    pin_led = LED(16)

    sensor_flujo = Button(pin_flujo_agua)
#~    
    while True:
        with open('Registro_de_agua.json') as file:
            ingreso = json.load(file)

        for i in ingreso['ajustes']:
            ajuste = int(i['alerta'])

        if sensor_flujo.when_pressed is True:
            x += 1
            datetime=datetime.now()
            flujo_agua_detectado(datetime, json)
            pin_led.on()
            if x >= ajuste:
                alerta_agua_detecado(datetime, json)
                x = 0

        elif sensor_flujo.when_pressed is False:
            pin_led.off()
            x = 0

#Inicio
imprimir()
