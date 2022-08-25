expo = int(input('Que raiz quieres conocer: '))
objetivo = int(input(f'Escoje un numero que quieras saber la raiz de {expo}: '))
numero = 0

while numero**expo < objetivo:
    numero += 1

if numero**expo == objetivo:
    print(f'El {objetivo} tiene raiz {expo} exacta y es {numero}')
    print(f'Resultado de {numero} elevado a {expo} es {numero**expo}')
else:
    print(f'El {objetivo} no tiene raiz {expo} exacta')