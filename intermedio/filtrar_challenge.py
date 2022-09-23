DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]


def run():
    # all_python_devs = [worker["name"] for worker in DATA if worker["language"] == "python"]
    all_python_devs = list(filter(lambda worker: worker["language"] == "python", DATA))
    all_python_devs = list(map(lambda worker: worker["name"], all_python_devs))
    
    # for worker in all_python_devs:
    #     print(worker)
    
    # all_platzi_devs = [worker["name"] for worker in DATA if worker["organization"] == "Platzi"]
    all_platzi_devs = list(filter(lambda worker: worker["organization"] == "Platzi", DATA))
    all_platzi_devs = list(map(lambda worker: worker["name"], all_platzi_devs))
    
    # for i in all_platzi_devs:
    #     print(i)
    
    # adults = list(filter(lambda worker: worker["age"] >= 18, DATA))
    # adults = list(map(lambda worker: worker["name"], adults))
    
    adults = [worker["name"] for worker in DATA if worker["age"] >= 18]
    
    # for worker in adults:
    #     print(worker)
    
    # old_people = list(map(lambda worker: worker | {"old": worker["age"] > 50}, DATA))
    # Esta es copiada porque la verdad no se me ocurria nada y fui a ver pero la entiendo lo suficiente para aplicarla con menores
    old_people = [worker | {"old": worker["age"] > 50} for worker in DATA]
    # Te preguntas que es eso tan raro y te dire nose, jaja no es que recuerdas que el profe dijo que añadieron este signo | para añadir dicionarios diccionarios nuevos, osea esta es la forma que se usaba antes para juntar diccionarios
# La sintaxis es x|y para añadir dicionarios a otros osea que x es tu diccionario actual y y es el diccionario nuevo que quieres añadir, si no entiendes y serian los items que vas añadir a tu diccionario x.
    # old_people = [{**worker, **{'old': worker['age'] > 70}} for worker in DATA]
    # print(old_people)
    # for worker in old_people:
    #     print(worker)
    
    # ejemplo de la misma funcion con menores de edad
    # young_people = [worker | {"young": worker["age"] <= 18} for worker in DATA]
    young_people = list(map(lambda worker: worker | {"young": worker["age"] <= 18}, DATA))
# Lo que esta sucediendo es para todos los trabajadores en DATA añade un nuevo key: young con el valor verdadero si son menores de 18 y un falso si son mayores de 18.
    for worker in young_people:
        print(worker)


if __name__ == '__main__':
    run()