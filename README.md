## Letter Guessing Game
This is a guessing game that asks the user to guess by letter to reveal the secret word
* You start by either choosing the category fruits or vegetables
* Depending if the user chose fruits or vegetables, a list of the one the user picked chooses a random element from the list and sets it to the secret word
* The code will show a number of dashes that represent the number of letters in the word
* Then it will prompt the user to start guessing by letter

### Guessing
* Incorrect Guess: They will **lose a chance** and will be told that the letter guessed is not in the secret word
* Correct Guess: The letter will then show up in the dashes where it is located in the word and the user will not lose a chance
    * If the letter guessed is in the word more than once, the letter will count for **all the times** it is in the word

#### Win vs Lose
* To win the game you must guess the word by letter in 9 chances
* You lose the game by running out of chances.

The code stores the user's guesses in a list and if the length of that list is equal to the length of thr secret word it will break out of the loop and you win
If the user runs out of guesses it will break out of the loop and tell the user they ran out if guesses
