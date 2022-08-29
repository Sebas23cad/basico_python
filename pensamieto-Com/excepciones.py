
from unicodedata import name

# Primer parte de excepciones con try y except
def divide_elementos(lista, divisor):
    try:
        return [i / divisor for i in lista]
    except ZeroDivisionError as e:
        print(e)
        return lista

lista = list(range(10))
divisor = 0

# print(divide_elementos(lista, divisor))

# Control de flujo y excepciones
def busca_pais(paises, pais):
    # &quot;&qout;&qout;
    # Paises es un diccionario. Pais es la llave.
    # Codigo con el principio EAFP.
    # &quot;&quot;&quot;
    
    try:
        return paises[pais]
    except KeyError:
        return None