import sys

def fibonnacci_recursivo(n):
    if n == 0 or n == 1:
        return 1
    
    return fibonnacci_recursivo(n - 1) + fibonnacci_recursivo(n - 2)

def fibonnacci_dinamico(n, memo = {}):
    if n == 0 or n == 1:
        return 1
    
    try:
        return memo[n]
    except KeyError:
        sys.setrecursionlimit(10002)
        resultado = fibonnacci_dinamico(n - 1, memo) + fibonnacci_dinamico(n - 2, memo)
        memo[n] = resultado
        
        return resultado


if __name__ == '__main__':
    n = int(input('Que numero quieres de fibonnacci: '))
    
    # resultado = fibonnacci_recursivo(n)
    resultado = fibonnacci_dinamico(n)
    print(resultado)