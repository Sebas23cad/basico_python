""" Try, except Es solo para los errores de typeerror """

# def palindromo(string):
#     return string == string[::-1]

# try:
#     print(palindromo(1))
# except TypeError:
#     print('Solo se puede hacer con texto')
    
""" Raise es elevar, y lo que hacemos seria elevar o declarar una excepcion que acinemos."""
def palindromo(string):
    try:
        if len(string) == 0:
            raise ValueError('No se puede ingresar una cadena vacia')
        return string == string[::-1]
    except ValueError as ve:
        print(ve)
        return False

try:
    print(palindromo(""))
except TypeError:
    print('Solo se puede hacer con texto')
    
""" Finally es muy rara de encontrar ya que la usamos para casos especiales como: cerrar un archivo, cerrar una coleccion a una base de datos o liberar recursos externos """

try:
    f = open("archivo.txt")
    # realizar cualquier cosa con el archivo
finally:
    f.close()