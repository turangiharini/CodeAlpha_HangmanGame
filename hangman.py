import random

# TASK 1: Hangman Game

def hangman():
    # Predefined list of words
    words = ["python", "hangman", "program", "challenge", "internship"]
    word = random.choice(words)  # Randomly select a word
    guessed = ["_"] * len(word)  # Hidden word display
    attempts = 6  # Limit of incorrect guesses
    used_letters = []  # Track guessed letters

    print("Welcome to Hangman!")
    print("Guess the word:", " ".join(guessed))
    print(f"You have {attempts} incorrect guesses allowed.")

    while attempts > 0 and "_" in guessed:
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue

        if guess in used_letters:
            print("You already guessed that letter.")
            continue

        used_letters.append(guess)

        if guess in word:
            print(f"Good job! '{guess}' is in the word.")
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed[i] = guess
        else:
            attempts -= 1
            print(f"Wrong guess! '{guess}' is not in the word. Attempts left: {attempts}")

        print("Word:", " ".join(guessed))
        print("Used letters:", ", ".join(used_letters))

    if "_" not in guessed:
        print("🎉 Congratulations! You guessed the word:", word)
    else:
        print("💀 Game Over! The word was:", word)

# Run the game
if __name__ == "__main__":
    hangman()
