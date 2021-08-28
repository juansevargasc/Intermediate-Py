def run():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {"firstname":"Facundo", "lastname":"García"}

    # Lista de diccionarios
    super_list = [
        {"firstname":"Facundo", "lastname":"García"},
        {"firstname":"Miguel", "lastname":"Torres"},
        {"firstname":"Pepe", "lastname":"Rodelo"},
        {"firstname":"Susana", "lastname":"Martínez"},
        {"firstname":"José", "lastname":"García"}

    ]

    # Diccionario de listas
    super_dict = {
        "natural_nums" : [1, 2, 3, 4, 5], 
        "integer_nums" : [-1, -2, 0, 3, 5],
        "floating_nums" : [1.1, 4.5, 6.43]
    }

    for key, value in super_dict.items():
        print(key, " - ", value)
    
    print("")

    for element in super_list:
        for key, value in element.items():
            print(key, " - ", value)
        

    

if __name__ == '__main__':
    run()