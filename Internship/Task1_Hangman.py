import random

def choose_word():
    words = ['python', 'hangman', 'programming', 'developer', 'algorithm']
    return random.choice(words).upper()

def display_word(word, guessed_letters):
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

def hangman():
    word = choose_word()
    guessed_letters = set()
    attempts_left = 6

    print("Welcome to Hangman!")
    print(display_word(word, guessed_letters))

    while attempts_left > 0:
        guess = input(f"Attempts left: {attempts_left}. Guess a letter: ").upper()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a valid single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("Correct!")
        else:
            attempts_left -= 1
            print("Incorrect!")

        current_display = display_word(word, guessed_letters)
        print(current_display)

        if '_' not in current_display:
            print("Congratulations! You've guessed the word!")
            break
    else:
        print(f"Game Over! The word was: {word}")

if __name__ == "__main__":
    hangman()
