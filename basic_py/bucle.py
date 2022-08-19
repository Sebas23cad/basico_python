# Ciclo while ejemplo
# def run(maximo):

#     esponente = 1

#     base = int(input('De que numero quieres saber su potencia: '))

#     resultado = 0

#     while (resultado < maximo):
#         print(f'este es el resultado {resultado}')
#         esponente += 1
#         resultado = base**esponente

# una constante en python se define con todas las letras en mayusculas, la definimos igual que una variable


# if __name__ == '__main__':
    # MAXIMO = int(input('Hasta que numero maximo quieres llegar: '))

    # run(MAXIMO)

# Ciclo for ejemplo

# def main(start, numero):
# Dos formas de hacer lo mismo

    # contador = 0

    # while contador < LIMITE:
    #     print(contador)
    #     contador += 1
# la linea de arriva es lo mismo que: contador = contador + 1

    # for contador in range(start, numero, 2):
    #     print(contador)

# Este ciclo tambien podemos usarlo para recorrer una cadena de caracteres o un string

def recorrer():
    frase = input('Escribe una frase: ')

    for i in frase:
        print(i.upper())


if __name__ == '__main__':
    # LIMITE = 1 + int(input('Hasta que numero quieres que se imprima en consola: '))

    # inicio = int(input('Desde que numero quieres que inicie: '))

    # run(LIMITE)

    # main(inicio, LIMITE)

    recorrer()