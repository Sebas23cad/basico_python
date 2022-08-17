def run(cantidad, monedas):

    dolares = cantidad / monedas
    dolares = round(dolares, 2)

    print(f'tus {tipo} son: {cantidad} que equivalen a {dolares}$ dolares')


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
        monedas = 4184.76
        tipo = 'Pesos colombianos'
    elif tipo == 2:
        monedas = 134.61
        tipo = 'Yen japones'
    elif tipo == 3:
        monedas = 6.8
        tipo = 'Yuan chino'
    elif tipo == 4:
        monedas = 19.14
        tipo = 'Libra egipcia'
    else:
        print('Erro, ingresa una opcion valida')

    cantidad = float(input(f'Caunto dinero tienes en {tipo} : '))

    run(cantidad, monedas)
