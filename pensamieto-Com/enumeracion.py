def enumeracion(objetivo): 
    EXPONENTE = 2
    numero = 0

    while numero**EXPONENTE < objetivo:
        numero += 1

    if numero**EXPONENTE == objetivo:
        print(f'El {objetivo} tiene raiz {EXPONENTE} exacta y es {numero}')
        print(f'Resultado de {numero} elevado a {EXPONENTE} es {numero**EXPONENTE}')
    else:
        print(f'El {objetivo} no tiene raiz {EXPONENTE} exacta')
