# Mi solucion
""" def run():
    llaves = []
    llaves = [i for i in range(1, 101)]
    valores = []
    valores = [i**3 for in range(1, 101)]
Estas dos soluciones son validas y nos da lo mismo, depende como a ti te guste lo puedes usar, pero las puse para que se vea que si conosco y se como usar ambos caminos.
    for i in range(1, 101):
        if i % 3 != 0:
            llaves.append(i)
    
    for valor in llaves:
        valores.append(valor**3)
        
    dict = {}

    h = 0
    while h < len(llaves):
        dict[llaves[h]] = valores[h]
        h += 1
        
    print(dict)   """ 

def main():
    """ # Soluion del profesor sin comprehension
    my_dict = {}

    for i in range(1, 101):
        if i%3 != 0:
            my_dict[i] = i**3 """

# solucion con dict comprehension
    my_dict = {i: i**3 for i in range(1, 101) if i%3 != 0}
        
    print(my_dict)


if __name__ == '__main__':
    # run()
    main()