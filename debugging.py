def divisors(num):
  divisor = []

  for i in range(1, num + 1):
    if num % i == 0:
      divisor.append(i)

  return divisor

def run():
  try:  
    num = int( input('Ingresa un número: ') )

    if num < 0:
      raise ValueError

    print(divisors(num))
    print('Termina mi programa')

  except ValueError:
    print('Debes ingresar un número entero positivo !')


if __name__ == '__main__':
  run()