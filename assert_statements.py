def divisors(num):
  divisor = []

  for i in range(1, num + 1):
    if num % i == 0:
      divisor.append(i)

  return divisor

def run():
  num = input('Ingresa un número: ') 
  assert num.isnumeric(), 'Debes ingresar un número'

  print( divisors( int(num) ) )
  print('Termina mi programa')
  

if __name__ == '__main__':
  run()
