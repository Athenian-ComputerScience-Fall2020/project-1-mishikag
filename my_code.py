# Collaborators (including web sites where you got help: (enter none if you didn't need help)
#  shanie lee

#intro

#incase user makes a typo, only lets them input food, animals, sports
def fun():
  category=input("please select your category. the categories are: fruit, vegetables, and drinks. ")
  if (category!="fruit" and category!="vegetables" and category!="drinks"):
    print("sorry, please enter either animals, food, or sports ")
    fun()

  elif category =="fruit":
    print("Okay, you have selected the mode animals. you have 9 chances to be wrong")
  elif category=="vegetables":
    print("Ok you have selected the mode food. You have 9 chances to be wrong")
  elif category=="drinks":
    print("Ok you have selected the mode sports. You have 9 chances to be wrong")

intro=input("hi. what is your name? ")
print("hello " + intro +". lets play the game!")

fun()

import random

# these are variables
chances=9
guesses=[]
win=0
guess=''
repeat=0

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
while win==0:
  letter_in_fruit =input("Okay, now please guess the letters of the name of the fruit you have "+str(chances)+" chances ")
  if letter_in_fruit in guesses:
    print("you already guessed this")

  else:
    repeat = 0
# this says that if a letter you guess is used multiple times in secretname, your guess will count for all of the times it is in the secretname
  for x in range(len(secretname)):
    if secretname[x] == letter_in_fruit:
      repeat+=1
      progress = progress[:x*2] + secretname[x] + progress[x*2 + 1:]

# this is if your guess is one of the letters in the secretname, then it will print the letter
  if letter_in_fruit in secretname:
    print(letter_in_fruit)

# else you lose a chance if it isn't one of the letters
  else:
    chances -= 1
    print("sorry, that is not one of the letters in the name. you have "+str(chances)+" more chances. ")

  print(progress)

# this puts your correct guess in a list
for x in range(repeat):
  guesses.append(letter_in_fruit)

# if the amount of correct guess is equal to the letters in the secretname, then win=1 meaning you won
  if len(secretname)==len(guesses):
    win=1
    print("great job, you got it!")
# you lose if you run out of chances and then win=1
  if chances==0:
    win=1
    print('sorry, you ran out of chances. you lose')
    print("this was the name " +secretname+ ".")
