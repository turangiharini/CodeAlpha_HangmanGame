# Hangman Game 🎮

## Overview
The Hangman Game is a classic word-guessing puzzle where the player tries to uncover a hidden word by guessing one letter at a time. The player has a limited number of incorrect guesses (6) before the game ends. This project is a simple text-based version implemented in Python.

## Features
- Random word selection from a predefined list.
- Tracks guessed letters and prevents duplicates.
- Allows up to 6 incorrect guesses.
- Displays progress after each guess.
- Console-based interaction (no graphics).

## How to Play
1. Run the program in your Python environment.
2. A random word will be chosen and displayed as underscores.
3. Enter one letter at a time to guess the word.
4. Correct guesses reveal letters in their positions.
5. Incorrect guesses reduce your remaining attempts.
6. Win by guessing the full word before attempts run out.

## Example Gameplay
Welcome to Hangman!
Guess the word: _ _ _ _ _ _
You have 6 incorrect guesses allowed.
Enter a letter: p
Good job! 'p' is in the word.
Word: p _ _ _ _ _
Used letters: p
...
🎉 Congratulations! You guessed the word: python

## Concepts Used
- **Random module** for word selection
- **While loop** for continuous gameplay
- **If-else conditions** for checking guesses
- **Strings and lists** for word handling
- **Input/Output** for user interaction

## Future Enhancements
- Add ASCII art for the hangman figure.
- Expand the word list.
- Include difficulty levels.

---

This project is beginner-friendly and demonstrates fundamental programming concepts in Python while keeping the gameplay fun and interactive.
