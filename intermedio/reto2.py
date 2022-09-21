import math

def run():
    my_dict = {i: math.sqrt(i) for i in range(1, 1001)}
    my_other_dict = {i: i**0.5 for i in range(1, 1001)}
    # print(my_dict)
    print(my_other_dict)


if __name__ == '__main__':
    run()