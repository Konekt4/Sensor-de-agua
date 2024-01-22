#Katana

#Se crea a partir de una función un archivo tipo Json para hacer el registro del flujo de agua y más
def json_crear(os, funcionamiento, json):
    
    #Variables para obtener la ruta donde se generará el archivo Json
    ruta = os.getcwd()
    contenido = os.listdir(ruta)

    #Ciclo for para buscar el archivo Json
    for archivo in contenido:
        #Si el archivo Json ya existía en este punto lo almacena en una lista llamada "Funcionamiento"
        if os.path.isfile(os.path.join(ruta, archivo)) and archivo.endswith('.json'):
            funcionamiento.append(archivo)

    # Preingreso de datos al archivo Json

    A = {}

    A['registro'] = []

    A['ajustes'] = [{"alerta" : "60"}]

    #Si no se encontró el archivo Json, lo crea automáticamente
    if "Registro_de_agua.json" not in funcionamiento:
        with open("Registro_de_agua.json", "w") as file:
            json.dump(A, file, indent=4)

#Función para llamar el programa e imprimir
def imprimir():
    programa()

#Función que hace posible el registro cuándo se activa el sensor de agua
def flujo_agua_detectado(datetime, json):
    #Se crea una lista para después ser almacenada en el archivo Json
    z = {}
    #Se prepara el archivo Json para guardar los registros de agua
    with open('Registro_de_agua.json') as file:
        salida = json.load(file)

    texto1 = "Flujo de agua detectado!"
    texto2 = str(datetime)
    print(texto1, texto2)
    z['aviso'] = texto1
    z['fecha'] = texto2
    salida['registro'].append(z.copy())
    
    #Se guarda la nueva información en el Json ya creado al principio del programa
    with open('Registro_de_agua.json','w') as file:
        json.dump(salida,file,indent=4)
    
#Función que crea una entrada especial, alerta, con el objetivo de distinguir un flujo anormal de agua
def alerta_agua_detecado(datetime, json):
    #Se crea una lista para después ser almacenada en el archivo Json
    y = {}
    #Se prepara el archivo Json para guardar los registros de agua
    with open('Registro_de_agua.json') as file:
        salida = json.load(file)

    texto1 = "Alerta!, flujo anormal de agua por tiempo prolongado detectado"
    texto2 = str(datetime)
    print(texto1, texto2)
    y['alerta'] = texto1
    y['fecha'] = texto2
    salida['registro'].append(y.copy())

    #Se guarda la nueva información en el Json ya creado al principio del programa
    with open('Registro_de_agua.json','w') as file:
        json.dump(salida,file,indent=4)

#Función programa que importa las librerías principales
def programa():
    from gpiozero import Button, LED
    import json
    import os
    from datetime import datetime
    funcionamiento = []

    #Se inicializa la variable para contar hasta la variable Alerta
    x = 0

    #Se llama la función para inicializar el Json
    json_crear(os, funcionamiento, json)

    pin_flujo_agua = 17
    pin_led = LED(16)

    sensor_flujo = Button(pin_flujo_agua)
#~  Se crea un bucle while para mantener operativo el programa
    while True:
        #Se abre el Json para obtener la variable ingreso
        with open('Registro_de_agua.json') as file:
            ingreso = json.load(file)

        #Se utiliza la variable ingreso para con un for obtener la variable ajuste que determina la alerta
        for i in ingreso['ajustes']:
            ajuste = int(i['alerta'])
        
        #Detección del agua
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

#Aquí se inicia el programa
imprimir()
