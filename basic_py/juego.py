import random

def run():
    aleatorio = random.randint(1, 100)
    usuario = int(input('Escribe un numero aleatorio del 1 al 100: '))
    while aleatorio != usuario:
        if aleatorio > usuario:
            usuario = int(input('Escoje un numero mas grande: '))
        elif aleatorio < usuario:
            usuario = int(input('Escoje un numero mas pequeño: '))
    print(f'Felicidades ganaste el numero era {aleatorio}')


if __name__ == '__main__':
    run()