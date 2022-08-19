def primo(numero):
    contador = 0

    for i in range(1, numero + 1):
        if i == 1 or i == numero:
            continue
        if numero % i == 0:
            contador += 1
            if contador >= 1:
                break
    if contador == 0:
        return True
    else:
        return False

def run():
    numero = int(input('Que numero quieres saber si es primo: '))

    if primo(numero):
        print(f'El numero {numero} es primo')
    else:
        print('El numero ' + str(numero) + ' no es primo')


if __name__ == '__main__':
    run()