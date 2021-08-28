DATA = [ # En mayúsculas para referirlo en que es constante.
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]

def run():
    all_python_devs = [ worker['name'] for worker in DATA if worker['language'] == 'python' ]
    all_platzi_workers = [worker['name'] for worker in DATA if worker['organization'] == 'Platzi' ]
    adults = list( filter(lambda worker: worker['age'] > 18, DATA) )
    adults = list( map(lambda worker: worker['name'], adults) ) 
    old_people = list( map(lambda worker: worker | {"old" : worker['age'] > 70 }, DATA)  ) # | pipe

    # The essential line of code is: worker | {"old" : worker['age'] > 70 }

    # Reto TO DO
    # 1. All python devs (names)
    all_python_devs2 = list( filter(lambda worker: worker['language'] == 'python', DATA) )
    all_python_devs2 = list( map(lambda worker: worker['name'], all_python_devs2) )

    # 2. All Platzi Workers
    all_platzi_workers2 = list( filter(lambda worker: worker['organization'] == 'Platzi', DATA) )
    all_platzi_workers2 = list( map(lambda worker: worker['name'], all_platzi_workers2) )
    
    # 3. Adults using list comprehensions
    adults2 = [worker['name'] for worker in DATA if worker['age'] > 18]
    old_people2 = [worker | {"old" : worker['age'] > 70 } for worker in DATA]

    for worker in old_people2:
        print( worker )


if __name__ == '__main__':
    run()