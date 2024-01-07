from gpiozero import Button
from signal import pause

pin_flujo_agua = 17

sensor_flujo = Button(pin_flujo_agua)

def flujo_agua_detectado():
    print("¡Flujo de agua detectado!")

sensor_flujo.when_pressed = flujo_agua_detectado

pause()