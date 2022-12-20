import random

def iniciar():
    palabra = "------"
    letra = input(f'''
Bienvenido al juego del ahoracado:
{palabra}
Escribe una letra: ''')
    escojer_palabra()
    return letra, palabra


def escojer_palabra():
    try:
        with open("./archivos/data.txt", "r", encoding="utf-8") as f:
            first_name = f.readlines()
        print(first_name)
        # Usar la funcion map con lamdab y rstrip para remover el salto de linea
    except FileNotFoundError:
        print('El archivo no existe')

    names = {i: first_name[i] for i in range(0, len(first_name))}

def run():
    iniciar()


if __name__ == '__main__':
    run()