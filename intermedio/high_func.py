from functools import reduce

# Utilizando list comprehension para filtrar.
my_list = [1, 4, 5, 6, 7, 8, 30, 21]

odd = [i for i in my_list if i%2 != 0]

print(odd)

# Utilizando la funcion filtrer

other_odd = list(filter(lambda x: x%2 != 0, my_list))

print(other_odd)

# utilizando la forma normal o que se para elevar al cuadrado una lista

other_list = [1, 5, 7, 4, 9]

potencia = [i**2 for i in other_list]

print(potencia)

# usando map para el mismo objetivo de elevar al cuadrado

squeres = list(map(lambda x: x**2, other_list))

print(squeres)

# utilizando una function para multiplicar las veces que nos digan.

new_list = [2, 2, 2, 2, 2]

all_multiplicad = 1

for i in new_list:
    all_multiplicad *= i
    
print(all_multiplicad)

# utilizando reduce

all_multiplied = reduce(lambda a, b: a * b, new_list)

print(all_multiplied)