from functools import reduce

def saludo(func):
    func()

def hola():
    print('Hola!!')

def adios():
    print('Adiós!!')

## Sacar los impares
def odd_numbers(the_list):
    odd = [i for i in the_list if i % 2 != 0]
    return odd

## Tomar los cuadrados
def squares(the_list):
    sq = [ i ** 2 for i in the_list ]
    print(sq)

## Filter
def filter_odd(a_list):
    odd = list( filter( lambda x: (x % 2) != 0, a_list ) )
    print(odd)

## Map
def map_squares(a_list):
    sq = list( map( lambda x: x**2, a_list ) )
    print(sq)

## Reduce
def all_multiplied(a_list):
    result = 1 # Neutral value

    for i in a_list:
        result *= i
    
    print(result)

def reduce_mult(a_list):
    result = reduce(lambda a, b: a * b, a_list)
    print(result)

if __name__ == '__main__':
    # List
    mylist = [1, 4, 5, 6, 9, 13, 19, 21]
    mylist2 = [1, 2, 3, 4, 5]
    twos = [2, 2, 2, 2, 2]

    # Función 1
    saludo(hola)
    saludo(adios)

    # Número impares, list comprehensions
    print(list)
    odd = odd_numbers(mylist)
    print(odd)

    # Número impares, filter
    print('FILTER')
    odd = filter_odd(mylist)
    print(odd)

    # Cuadrados
    squares(mylist2)

    # Cuadrados map
    print('MAP')
    map_squares(mylist2)

    # Multiplicación de elementos de una lista
    print(f'Multiplication: {twos} = ')
    all_multiplied(twos)

    # Reduce
    print(f'Multiplication: {twos} = ')
    reduce_mult(twos)
