import random

words = ["apple", "tiger", "house", "robot", "pizza"]

word = random.choice(words)

guessed_letters = []

display = ["_"] * len(word)

incorrect_guesses = 0
max_incorrect = 6

print("Welcome to Hangman!")

while incorrect_guesses < max_incorrect and "_" in display:
    print("\nWord:", " ".join(display))
    print("Incorrect guesses left:", max_incorrect - incorrect_guesses)

    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct!")
        for i in range(len(word)):
            if word[i] == guess:
                display[i] = guess
    else:
        print("Wrong!")
        incorrect_guesses += 1

if "_" not in display:
    print("\nCongratulations! You guessed the word:", word)
else:
    print("\nGame Over! The word was:", word)
