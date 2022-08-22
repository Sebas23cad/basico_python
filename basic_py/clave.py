# Asi creamos una lista
# Para acceder a una lista lo hacemos asi, tambien tenemos mas cosas que podemos hacer con una lista:
# lista[start:end:steps] Es parecido a los slides
# lista = [a, b , etc]
# Asi creamos una tuple y asi la recoremos, tambien tenemos metodos en las mismas:
# tupla = (a, b, etc)
# Recuerda las tuplas son inmutalbles y las listas son mutables
# tupla[s:e:st] Es igual que las listas para acceder a los valores
# Asi creamos los diccionarios y tambien tenemos metodos para cada uno:
# diccionario = {
#   'key' = value,
# }
# En los diccionarios tenemos diferentes metodos y no podemos acceder con indices a sus valores.
import random

def generar():
    MAYUS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']
    MINUS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']
    NUMS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    CHARS = ['*', '+', '-', '/', '@', '_', '?', '!', '[', '{', '(', ')', '}', ']', ',', ';', '.', '>', '<', '~', '°', '^', '&', '$', '#', '"']

    lista = MAYUS + MINUS + NUMS + CHARS

    contrasena = []

    for i in range(15):
        caracter_random = random.choice(lista)
        contrasena.append(caracter_random)

    contrasena = ''.join(contrasena)
    return contrasena

def run():
    contrasena = generar()
    print(f'Tu nueva contraseña es: {contrasena}')

if __name__ == '__main__':
    run()