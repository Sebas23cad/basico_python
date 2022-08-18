def run(cantidad, valor):

    dolares = cantidad / valor
    dolares = str(round(dolares, 2))

    print(f'tus {tipo} son: {str(cantidad)} que equivalen a {dolares}$ dolares')


if __name__ == '__main__':

    # moneda = dict()

    moneda = {
        'Pesos colombianos': 1,
        'Yen japones': 2,
        'Yuan chino': 3,
        'Libra egipcia': 4,
    }

    tipo = int(input(f'Que moneda tienes: {moneda.items()} : '))

    if tipo == 1:
        valor = 4184.76
        tipo = 'Pesos colombianos'
    elif tipo == 2:
        valor = 134.61
        tipo = 'Yen japones'
    elif tipo == 3:
        valor = 6.8
        tipo = 'Yuan chino'
    elif tipo == 4:
        valor = 19.14
        tipo = 'Libra egipcia'
    else:
        print('Error la opcion no existe, ingresa una opcion valida')

    cantidad = float(input(f'Caunto dinero tienes en {tipo} : '))

    run(cantidad, valor)
    