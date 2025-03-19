Word Guessing Game in Python

Description

The Word Guessing Game is a simple Python program where the player tries to guess a randomly chosen animal name by guessing individual letters. The game provides a limited number of attempts, and the player must correctly guess all the letters before running out of chances.

Features

Randomly selects an animal name from a predefined list.

Allows the user to guess one letter at a time.

Displays the word's progress with guessed letters revealed.

Limits the number of incorrect attempts to 15.

Provides feedback on correct and incorrect guesses.

Prevents duplicate guesses.

Case-insensitive letter matching.

Displays the correct word when the player loses.

How to Play

Run the Python script.

Enter your name when prompted.

Try to guess the hidden word by entering one letter at a time.

If the letter is in the word, it will be revealed in its correct position.

If the letter is incorrect, your remaining attempts decrease.

Continue guessing until you either guess the full word or run out of attempts.

The game will display whether you won or lost.

Prerequisites

Python 3.x installed on your system.

How to Run the Game

Download or clone this repository.

Open a terminal or command prompt.

Navigate to the script's directory.

Run the script using:

python word_guessing_game.py

Follow the on-screen instructions to play.

Example Output

Enter your name: Alice
Good luck, Alice!

Guess the word:
- - - - - -

Guess a letter: a
Correct guess!
A - - - - -
Remaining attempts: 14

Guess a letter: e
Incorrect guess!
A - - - - -
Remaining attempts: 13
...

Future Enhancements

Add difficulty levels with varying word lengths and attempt limits.

Implement a graphical interface for a better user experience.

Allow the user to choose different word categories.

