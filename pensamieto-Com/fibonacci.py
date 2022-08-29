def fibonaci(n):
    """Calcula la serie de fibonaci

    n int > 0
    la manera mas simple de escribir la serie de fibonacci
    """
    
    if n == 0 or n == 1:
        return 1
    print(n)
    
    return fibonaci(n - 1) + fibonaci(n - 2)

n = int(input('Que numero en la serie de fibonacci quieres: '))

print(fibonaci(n))