def divisors(num):
    divisiones = [ i for i in range(1, num + 1) if num % i == 0]
    return divisiones

""" def run():
    num = input('Escribe un numero: ')
# Usamos un metodo de los string para saber si es un numero o letra, y nos devuelve verdadero o falso en corde lo que sea.
    assert num.isnumeric(), 'Debes ingresar un numero'
# Lo que hacemos es transformar despues a un numero ya que el metodo es de strings y con el nos aseguramos que sea cualquier tipo de numero.
    print(divisors(int(num)))
    print('Termino el programa') """
    
def run():
    num = int(input('Ingresa un numero: '))
    assert num >= 1, 'Solo aceptamos numeros positivos'
    print(divisors(num))
    print('Termino todo')


if __name__ == '__main__':
    run()