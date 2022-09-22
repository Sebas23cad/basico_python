# Ejemplo de lambda con un palindromo

from cgi import print_form


palindromo = lambda string: string == string[::-1]

print(palindromo('ana'))

# El mismo ejemplo sin lambda

def palindrome(string):
    return string == string[::-1]

print(palindrome('ana'))

# Este es mi ejemplo practico jaja

suma = lambda numero: numero + 3

print(suma(4))