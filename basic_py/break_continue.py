def run():
    # Aqui imprimimos solo los numeros impares por que todos los numeros pares su modulo es sero y decimos que si el modulo es cero no lo haga y si no que continue
    # for i in range(100):
    #     if i % 2 == 0:
    #         continue
    #     print(i)

    # Aqui vamos a utilizar el break para cortar el ciclo en un numero que necesitemos como podria ser un resultado o algo parecido que necesitemos un valor especifico en un conjunto
    # for contador in range(1000):
    #     print(contador)
    #     if contador == 560:
    #         break

    # texto = input('Escribe un texto: ')

    # for letra in texto:
    #     if letra == 'e':
    #         break
    #     print(letra)

    # Utilizaremos las palabras en un ciclo while

    contador = 0

    while contador < 100:
        contador += 1
        print(contador)

        if contador == 30:
            break


if __name__ == '__main__':
    run()