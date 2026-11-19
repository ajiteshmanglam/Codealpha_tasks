import random


def play_hangman():
    words = ["python", "planet", "guitar", "castle", "bridge"]
    secret_word = random.choice(words)

    guessed_letters = []
    incorrect_guesses = 0
    max_incorrect = 6

    print("Welcome to Hangman!")
    print(f"Guess the word one letter at a time. You have {max_incorrect} incorrect guesses allowed.\n")

    while incorrect_guesses < max_incorrect:
        display_word = [letter if letter in guessed_letters else "_" for letter in secret_word]
        print("Word:", " ".join(display_word))
        print(f"Incorrect guesses left: {max_incorrect - incorrect_guesses}")
        if guessed_letters:
            print("Guessed letters:", ", ".join(sorted(guessed_letters)))

        if "_" not in display_word:
            print(f"\nCongratulations! You guessed the word: {secret_word}")
            break

        guess = input("\nEnter a letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.\n")
            continue

        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try another letter.\n")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:
            print(f"Good guess! '{guess}' is in the word.\n")
        else:
            incorrect_guesses += 1
            print(f"Sorry, '{guess}' is not in the word.\n")
    else:
        print(f"Game over! You ran out of guesses. The word was: {secret_word}")


if __name__ == "__main__":
    play_hangman()