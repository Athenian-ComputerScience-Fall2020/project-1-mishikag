* Importing a module: random

* Define the function introduction

* Input the question are you ready to play the game

* Define the function fun
    * Make the variable category global
	* Make the input category an integer and have the user select the category. 1 for fruit, 2 for vegetables
	* If input category is 1
		* Then print that the user has selected fruit
	* If input category is 2
		* Then print that the user has selected vegetables

* Try for an error
	* Call the function

* If the code catches an error
	* Print that the user must enter an integer
	* Call the function

* After the function is called, if the category equals 1

* Define the variables:
	* Chances is equal to 9
	* Guesses is an empty list
	* Repeat is equal to zero

* Call the function introduction to ask if the user is ready to play the game
* Give the list fruit the elements: kiwi, mango, strawberries, apples, bananas, pears, watermelons, grapes, and oranges
* X is a random element from the start of the list to the last element
* List of x fruit is redefined to secret name

* Progress is equal to an empty string

* For the number of letters in secret name
	* Progress now equals **_** and progress
	* Print the number of dashes

* While the secret name does not equal guesses
	* The input letter in fruit asks the user to start guessing a letter and tells the user how many chances they have
	* for x in range of the length of the secret name
			* If secret name of x equals the input letter in fruit
			    * Progress is now taking the values in those positions of the lists and adding it into progress
                * Append the users correct guesses into the list “guesses” from the input letter in fruit
		* If the input letter in fruit is in the secret name
			* Then print the letter
		* Else
			* Lose one chance
			* Print that the guess is not one of the letters in the secret word, and tell the user how many chances they have left

		* Print progress

		* If the length of the secret word is equal to the length of the list guesses
			* Break out of the loop

		* If chances are equal to zero
			* Break out of the loop


    * If the length of the secret word is equal to the length of the list guesses
	    * Print great job, you got it!

	* If chances are equal to zero
		* Print sorry, you ran out if guesses. You lose
		* Print what the secret word was
