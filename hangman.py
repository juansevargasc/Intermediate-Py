# My Workflow. Juanse
'''  
Here I'm going to document my steps.

1. First I brought in the read and write functions, in order to read the words from the text 
   and to write words already opened.
2. Second I create a function to take a word radonmly from the list.

3. Create the game dynamic. Print the word underscore lines and ask for the letter. Function: "guessWord()".

'''
import numpy as np
import random
import os

def readText(route):
  list_text = []
  with open(route, 'r', encoding='utf-8') as f:
    for line in f:
      list_text.append( line )
      #print(line)
  #print(list_text)
  return list_text

def write(route, content):
  with open(route, 'a', encoding='utf-8') as f:
    names = content
    for name in names:
      f.write(name)
      f.write('\n')

def pickAWord(words):  
  word = random.choice(words)
  return word


'''
  Function that creates the game dynamic.
  1. Takes the word length.
  2. Prints underscore of the word.
  3. Create a boolean variable guessing.
  4. Create the while loop. We check if word is guessed or if the maximum number of opportunities is reached.

'''
def guessWord(word, maxAttempts):
  lengthOfWord = len(word) - 1 # Without \n
  word = word.replace('\n', '') # Getting rid of \n

  # Necessary Variables 
  attempts = 0
  stillGuessing = True # We start guessing.
  wordInList = [char for char in word]  # Storing the word we're gonna play with, as a list of letters.
  wordDictionary = {} # Storing a dictionary with the index
  for count, value in enumerate(wordInList):
    wordDictionary[count] = value
  notGuessed = [] # Storing the underscore places related to the word. It'll be filled until is guessed or points are out.
  # Filling underscore array
  for _ in range(lengthOfWord):
    notGuessed.append('_')
  
  #print(underscorePrint)
  print(wordDictionary)

  while(stillGuessing):
    # Prints underscore
    os.system("clear")
    print(f'Intentos: {attempts}')
    print(notGuessed)
    # Asks to write a letter. If not alphanumeric returns an error.
    letter = input('Ingresa tu letra: ') 
    assert letter.isalpha(), 'Debes ingresar una letra'
    
    # If the letter matches, then we remove the notGuessed letters
    for i in wordDictionary.keys():
      let = wordDictionary[i]
      if let == letter:
        notGuessed.pop(i)
        notGuessed.insert(i, let)
          
    if attempts > maxAttempts:
          stillGuessing = False
          print('Se ahorcó, alcanzaste el número máximo de intentos') 
    elif ('_' in notGuessed) == False:
          stillGuessing = False
          os.system("clear")
          print('Ganaste!!')
          print(f'La palabra es: {word.upper()} ')
    attempts += 1
  
  print('END')

    #
    #print(underscorePrint)

  
  


def run():
  # For tests
  print("jimeno")
  names = ['Mario', 'Juanse', 'Miguel', 'Esteban', 'Carlos']
  list_names = np.array(names)

  # Read text and print it
  words = readText('./archivos/data.txt')
  words = np.array(words)
  print(words.size)
  random.seed(271)
  print(random.randrange(10))
  
  # Random function chooses a word
  word = pickAWord(words)
  
  #TESTING
  print(word)
  print(len(word))
  guessWord(word, 4) # actually workingggg

  
  #for i in range(5):
   # print(pickAWord(words))



if __name__ == "__main__":
  run()

