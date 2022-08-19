def run(palabra):
    palabra = palabra.lower().replace(' ', '')
    frase_reves = palabra[::-1]

    if palabra == frase_reves:
        print(f'La palabra {palabra} es el palindromo de {frase_reves}')
    else:
        print('No son palindromos, son diferentes')


if __name__ == '__main__':
    frase = str(input('Que palabra quieres: '))

    run(frase)