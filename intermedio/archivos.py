def read():
    numbers = []
# El ultimo atributo es mas que todo para cuando tengamos caracteres especiales y queramos leerlos y no se nos dañe nuestro programa. Los que sepan css saben que es para que entienda eñ español con emojisy signos.
    with open("./archivos/numbers.txt", "r", encoding="utf-8") as f:
        for line in f:
            numbers.append(int(line))
    print(numbers)


def write():
    names = ['Mateo', 'Facundo', 'Sebastian', 'Marco', 'Mauricio', 'José']
    with open("./archivos/names.txt", "a", encoding="utf-8") as f:
        for name in names:
            f.write(name)
            # El de habajo es para crear un salto de linea
            f.write("\n")


def run():
    write()


if __name__ == '__main__':
    run()