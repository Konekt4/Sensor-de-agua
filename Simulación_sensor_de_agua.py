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
    import json
    import os
    from msvcrt import getch
    from datetime import datetime
    funcionamiento = []

    uno = b'1'
    cero = b'0'
    x = 0

    json_crear(os, funcionamiento, json)
    
    pin_led = "Foco"
 #⌂           
    while True:
        with open('Registro_de_agua.json') as file:
            ingreso = json.load(file)

        for i in ingreso['ajustes']:
            ajuste = int(i['alerta'])

        print(x)
        print("Ingrese 1 o 0 ----> ")
        sensor_flujo = getch()
        if sensor_flujo == uno:
            x += 1
            datetime=datetime.now()
            flujo_agua_detectado(datetime, json)
            print(pin_led," prendido")
            if x >= ajuste:
                alerta_agua_detecado(datetime, json)
                x = 0
            

        elif sensor_flujo == cero:
            print(x)
            print(pin_led," apagado")
            x = 0
            print(x)

#Inicio
imprimir()
