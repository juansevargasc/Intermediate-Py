import numpy as np


def run():
  print("jimeno")
  names = ['Mario', 'Juanse', 'Miguel', 'Esteban', 'Carlos']
  list_names = np.array(names)
  wordInList = {}

  for count, value in enumerate(names):
    wordInList[count] = value

  print(list_names)
  print(wordInList)

  for i in wordInList.keys():
    print(i)
  
  print('_' in names)

if __name__ == "__main__":
  run()