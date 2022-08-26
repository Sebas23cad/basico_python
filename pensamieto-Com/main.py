from aproximacion import aproximacion
from enumeracion import enumeracion
from binaria import binario
opciones = '''Que solucion de busqueda te gusta:
    1.Busqueda binaria:
    2.Aproximacion: 
    3.Enumeracion: '''

def run():
    solucion = int(input(f'{opciones}'))
    
    if solucion == 1:
        objetivo = int(input('Cual es tu objetivo: '))
        binario(objetivo)
    elif solucion == 2:
        objetivo = int(input('Cual es tu objetivo: '))
        aproximacion(objetivo)
    elif solucion == 3:
        objetivo = int(input('Cual es tu objetivo: '))
        enumeracion(objetivo)
    else:
        print('Porfavor escoje una opcion valida')


if __name__ == '__main__':
    run()