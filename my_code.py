# Collaborators (including web sites where you got help: (enter none if you didn't need help)
#  shanie lee
#code doesn't stop when you win and code doesn't do anything when you enter a letter you already guessed

#introduction to the game

import random

def introduction():
    intro = input("Are you ready to play the game? ")

#this trys for bad user input
def fun():
  global category
  category=int(input("please select your category. the categories are: fruit or vegetables. enter 1 for fruit and 2 for vegetables "))
  if category ==1:
    print("Okay, you have selected the mode fruit.")
  elif category==2:
    print("Ok you have selected the mode vegetables.")

try:
  fun()
#prints that you have to enter the correct input and then runs the function again
except:
  print("sorry, please enter either fruit or vegetables ")
  fun()

if category ==1:

  # these are variables
  chances=9
  guesses=[]
  repeat = 0

  introduction()

  # this is the list of possibilities that you would have to find
  fruit = ["kiwi","pineapple","mango","strawberries","apples","bananas","pears","watermelon","grapes", "oranges"]
  x = random.randint(0, len(fruit)-1) #this just means that x is a random element from the list from first to last
  secretname=fruit[x]
  print(secretname)

  # this prints the dashes for the number of letter in secretname everytime you guess, and if you get letters correct, it replaces the dash with a letter
  progress = ""
  for letter in secretname:
    progress = "_ " + progress
    print("_ ")

  #this tells you to start guessing
  while secretname!=guesses:
    print(secretname) #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    print(guesses)

    letter_in_fruit =input("Okay, now please guess the letters of the name of the fruit you have "+str(chances)+" chances ")

  # this says that if a letter you guess is used multiple times in secretname, your guess will count for all of the times it is in the secretname
    for x in range(len(secretname)):
      if secretname[x] == letter_in_fruit:
        progress = progress[:x*2] + secretname[x] + progress[x*2 + 1:]
        guesses.append(letter_in_fruit)

  # this is if your guess is one of the letters in the secretname, then it will print the letter
    if letter_in_fruit in secretname:
      print(letter_in_fruit)
  # else you lose a chance if it isn't one of the letters
    else:
      chances -= 1
      print("sorry, that is not one of the letters in the name. you have "+str(chances)+" more chances. ")

    print(progress)

  # this puts your correct guess in a list
   # if letter_in_fruit in secretname:
    #  guesses.append(letter_in_fruit)

    if len(secretname)==len(guesses):
      break
    if chances==0:
      break

  # if the amount of correct guess is equal to the letters in the secretname then you win
  if len(secretname)==len(guesses):
    print("great job, you got it!")

  # you lose if you run out of chances
  if chances==0:
    print('sorry, you ran out of chances. you lose')
    print("the word was " +secretname+ ".")

if category ==2:

  # these are variables
  chances=9
  guesses=[]
  repeat = 0

  introduction()

  # this is the list of possibilities that you would have to find
  vegetables = ["broccoli","pepper","lettuce","carrot","garlic","potato","cauliflower","cucumber","spinach", "zucchini"]
  x = random.randint(0, len(vegetables)-1) #this just means that x is a random element from the list from first to last
  secretname=vegetables[x]
  print(secretname)

  # this prints the dashes for the number of letter in secretname everytime you guess, and if you get letters correct, it replaces the dash with a letter
  progress = ""
  for letter in secretname:
    progress = "_ " + progress
    print("_ ")

  #this tells you to start guessing
  while secretname!=guesses:
    print(secretname) #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    print(guesses)

    letter_in_vegetables =input("Okay, now please guess the letters of the name of the fruit you have "+str(chances)+" chances ")

  # this says that if a letter you guess is used multiple times in secretname, your guess will count for all of the times it is in the secretname
    for x in range(len(secretname)):
      if secretname[x] == letter_in_vegetables:
        progress = progress[:x*2] + secretname[x] + progress[x*2 + 1:]
        guesses.append(letter_in_vegetables)

  # this is if your guess is one of the letters in the secretname, then it will print the letter
    if letter_in_vegetables in secretname:
      print(letter_in_vegetables)
  # else you lose a chance if it isn't one of the letters
    else:
      chances -= 1
      print("sorry, that is not one of the letters in the name. you have "+str(chances)+" more chances. ")

    print(progress)

  # this puts your correct guess in a list
   # if letter_in_fruit in secretname:
    #  guesses.append(letter_in_fruit)

    if len(secretname)==len(guesses):
      break
    if chances==0:
      break

  # if the amount of correct guess is equal to the letters in the secretname then you win
if len(secretname)==len(guesses):
  print("great job, you got it!")

  # you lose if you run out of chances
if chances==0:
  print('sorry, you ran out of chances. you lose')
  print("the word was " +secretname+ ".")
