def run():
    squares = [i for i in range(1, 10000) if i % 4 == 0 and i % 6 == 0 and i % 9 == 0]
    
    print(squares)
    
    other_squares = [j for j in range(1, 10000) if j % 36 == 0]
    
    print(other_squares)


if __name__ == '__main__':
    run()