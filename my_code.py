# Collaborators (including web sites where you got help: (enter none if you didn't need help)
#  shanie lee
#code doesn't stop when you win and code doesn't do anything when you enter a letter you already guessed

#introduction to the game
def introduction():
    intro = input("hi. what is your name? ")
    print("hello " + intro +". lets play the game!")
introduction()
#this trys for bad user input
try:
  def fun():
    category=input("please select your category. the categories are: fruit, vegetables, and drinks. ")
    if (category!="fruit" and category!="vegetables" and category!="drinks"):
      print("sorry, please enter either animals, food, or sports ")
      fun()
    elif category =="fruit":
      print("Okay, you have selected the mode fruit. you have 9 chances to be wrong")
    elif category=="vegetables":
      print("Ok you have selected the mode vegetables. You have 9 chances to be wrong")
    elif category=="drinks":
      print("Ok you have selected the mode drinks. You have 9 chances to be wrong")
#prints that you have to enter the correct input and then runs the function again

except:
  print("sorry you must enter fruit, vegetables, or drinks")
  fun()
else:
  fun()

import random

# these are variables
chances=9
guesses=[]
guess=''

# this is the list of possibilities that you would have to find
fruit = ["kiwi","pineapple","mango","strawberries","apples","bananas","pears","watermelon","grapes", "oranges"]
x = random.randint(0, len(fruit)-1)
secretname=fruit[x]
print(secretname)

# this prints the dashes for the number of letter in secretname everytime you guess, and if you get letters correct, it replaces the dash with a letter
progress = ""
for letter in secretname:
  progress = "_ " + progress
  print("_ ")

#this tells you to start guessing
while chances > 0:
  letter_in_fruit =input("Okay, now please guess the letters of the name of the fruit you have "+str(chances)+" chances ")
#if
  if letter_in_fruit in guesses:
    print("you already guessed this")

# this says that if a letter you guess is used multiple times in secretname, your guess will count for all of the times it is in the secretname
  for x in range(len(secretname)):
    if secretname[x] == letter_in_fruit:
      progress = progress[:x*2] + secretname[x] + progress[x*2 + 1:]

# this is if your guess is one of the letters in the secretname, then it will print the letter
  if letter_in_fruit in secretname:
    print(letter_in_fruit)

# else you lose a chance if it isn't one of the letters
  else:
    chances -= 1
    print("sorry, that is not one of the letters in the name. you have "+str(chances)+" more chances. ")
  if len(secretname)==len(guesses):
    break

  print(progress)

# this puts your correct guess in a list
guesses.append(letter_in_fruit)

# if the amount of correct guess is equal to the letters in the secretname then you win
if len(secretname)==len(guesses):
  print("great job, you got it!")

# you lose if you run out of chances
if chances==0:
  print('sorry, you ran out of chances. you lose')
  print("this was the word " +secretname+ ".")
