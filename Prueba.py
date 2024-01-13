from msvcrt import getch

uno = b'1'
cero = b'0'

while True:
    entrada = getch()
    print(entrada)
    if entrada == uno:
        print("Uno presionado")
    elif entrada == cero:
        print("Cero presionado")