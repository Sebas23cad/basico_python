""" def divisors(num):
    # Para los errores lo que hacemos es revisar el programa linea por linea, hasta encontrarlo o usar run and debug a la parte izquierda de nuestro editor
    divisors = []
    # divisors = [i for i in range(1, num + 1) if num % i == 1]
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors

def run():
    num = int(input('Ingresa un numero: '))
    print(divisors(num))
    print('Termino mi programa')


if __name__ == '__main__':
    run() """ 

""" def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors

# Mi solucion :)

def run():
    num = input('Ingresa un numero: ')
    # print(divisors(num))
    # print('Termino mi programa')
    try:
        if type(num) == str:
            raise ValueError('Solo admite numeros')
        return print(divisors(num))
    except ValueError as ve:
        print(ve)
        return False """


    
def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors

""" def run():
    try:
        num = int(input('Escribe un numero: '))
        print(divisors(num))
        print('Termino el programa')
    except ValueError:
        print('Debes ingresar un numero') """

def run():
    try:
        num = int(input('Escribe un numero: '))
        if num <= 0:
            raise ValueError('No admitimos numeros negativos')
        return print(divisors(num))
    except ValueError as ve:
        print(ve)
        print('Debes ingresar un numero')
        return False
        

if __name__ == '__main__':
    run()