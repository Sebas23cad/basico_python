# Esta es mi solucion si lo compruebas son todas las potencias de los 101 primeros numeros jaja
""" def run():
    numeros = []
    for i in range(1,101):
        print(i)
        i += 1
        numeros.append(i)
    
    for valores in numeros:
        resultado = valores**2
        print(resultado)


if __name__ == '__main__':
    run() """
    
# Solucion del ejercicio por parte del profesor

def main():
    """ 
    squares = []
    for i in range(1, 101):
        # Esta es mi solucion
        valor = i**2
        if valor % 3 == 0:
            continue
        squares.append(i**2)
        if i % 3 != 0:
            squares.append(i**2) """
            
    # utilizando list comprehension en una sola linea
    squares = [i**2 for i in range(1, 101) if i % 3 != 0]

    print(squares)


if __name__ == '__main__':
    main()