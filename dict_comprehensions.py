from math import sqrt

def run():
    my_dict = {}

    for i in range(1, 101):
        if i % 3 != 0:
            my_dict[i] = i ** 3

    print(my_dict) # print

def reto():
    my_dict = {i : i ** 3 for i in range(1, 101) if i % 3 != 0}
    print(my_dict)

def reto2():
    my_dict = {i : sqrt(i) for i in range(1, 101) }
    print(my_dict)

if __name__ == '__main__':
    #run() 
    #reto()
    reto2()