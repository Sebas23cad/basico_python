def run():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {"firstname": "Manolo", "lastname": "Garcia"}

# Creamos una lista que almacena diccionarios
    super_list = [
        {"firstname": "Manolo", "lastname": "Garcia"},
        {"firstname": "Juancho", "lastname": "Cabezas"},
        {"firstname": "Camilo", "lastname": "Camacho"},
        {"firstname": "Mauricio", "lastname": "Marquez"},
        {"firstname": "Matilda", "lastname": "Morocho"},
        {"firstname": "Dolores", "lastname": "Delano"}
    ]
    
# Creamos un diccionario que almacena listas
    super_dict = {
        "natural_nums": [1, 2, 3, 4, 5],
        "Interger_nums": [-2, -1, 0, 1, 2],
        "floating_nums": [1.2, 2.3, 4.6, 1.3]
    }
    
# Recoremos el diccionario valor por valor
    for key, value in super_dict.items():
        print(f'{key} - {value}')
        
# Recorrer la lista
    for values in super_list:
        for key, value in values.items():
            print(f'{key} - {value}')


if __name__ == '__main__':
    run()