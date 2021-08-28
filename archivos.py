def read():
  numbers = []
  with open('curso-intermedio-py/archivos/numbers.txt', 'r', encoding='utf-8') as f:
    for line in f:
      numbers.append(int(line))
  print(numbers)

def write():
  names = ['Mario', 'Juanse', 'Miguel', 'Esteban', 'Carlos']
  with open('curso-intermedio-py/archivos/names.txt', 'a', encoding='utf-8') as f:
    for name in names:
      f.write(name)
      f.write('\n')

def run():
  write()


if __name__ == '__main__':
  run()