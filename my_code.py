# Collaborators (including web sites where you got help: (enter none if you didn't need help)
#  shanie lee

#intro

intro=input("hi. what is your name? ")
print("hello " + intro +". lets play the game!")
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
fun()

import random

chances = 9
guesses = []
win = 0
repeat = 0

fruit = ["kiwi","pineapple","mango","strawberries","apples","bananas","pears","watermelon","grapes", "oranges"]
x = random.randint(0, len(fruit)-1)
secret_name=fruit[x]

progress = ""
for letter in secret_name:
  progress = " _ " + progress
  print(" _ ")

while win==0:
    letter_in_person =input("Okay, now please guess the letters of the name of the person you have "+str(chances)+" chances ")
    if letter_in_person in guesses:
        print("you already guessed this")
    else:
      repeat = 0
# this says that if a letter you guess is used multiple times in secretname, your guess will count for all of the times it is in the secretname
    for x in range(len(secret_name)):
        if secret_name[x] == letter_in_person:
            repeat+=1
            #part to go through word and see if letter is there more than once
    # this is if your guess is one of the letters in the secretname, then it will print the letter
    if letter_in_person in secret_name:
        print(letter_in_person)

# else you lose a chance if it isn't one of the letters
    else:
        chances -= 1
        print("sorry, that is not one of the letters in the name. you have ",chances," more chances. ")
        print(progress)








