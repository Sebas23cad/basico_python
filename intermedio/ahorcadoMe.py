import random

def iniciar():
    inicio = input('''
Adivina la palabra
------------
Ingresa una letra: ''')
    diccionario()
    return inicio

def diccionario():
    with open("./archivos/data.txt", "r", encoding="utf-8") as f:
        names = [line for line in f]
    return names

def adivina(letra, palabras):
    palabra = random.randint(0, len(palabras))
    print(palabra)


def run():
    iniciar()


if __name__ == '__main__':
    run()