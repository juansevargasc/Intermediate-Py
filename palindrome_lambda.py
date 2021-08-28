
def palindrome(word):
    if word == word[ : : -1]:
        return True
    return False

variable = lambda string: string == string[ : : -1]
variable2 = lambda cadena: cadena == cadena[: : -1]

def run():
    # Input
    palabra = input('¿Es palíndroma? ')
    
    # Función normal
    b = palindrome(palabra)
    print(b)

    # Función Anónima para evaluar un palíndromo:
    print( variable2(palabra) )
    

if __name__ == '__main__':
    run()