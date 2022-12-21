import random


def escojer_palabra():
    try:
        with open("./archivos/data.txt", "r", encoding="utf-8") as f:
            first_name = f.readlines()
        # Usar la funcion map con lamdab y rstrip para remover el salto de linea
        names = list(map(lambda l: l.rstrip("\n"), first_name))
        dict_names = {i+1: name for i, name in enumerate(names)}
        numero = random.randint(1, len(dict_names))
        palabra_escojida = dict_names.get(numero)
        return palabra_escojida
    except FileNotFoundError:
        print('El archivo no existe')


# Terminamos de escojer una palabra al azar y ya la tenemos en una variable nos falta modificar, el numero de - para cada palabra y tambien nos queda por limpiar la pantalla y que valla cambiando cada rallita por la letra.
def iniciar():
    palabra = escojer_palabra()
    letra = input(f'''
Bienvenido al juego del ahoracado:
{palabra}
Escribe una letra: ''')
    return letra, palabra


def run():
    iniciar()


if __name__ == '__main__':
    run()