import random
from words import word_list

def get_word():
    word = random.choice(word_list)
    return word.upper()

def play(word):
    word_completion = "_" * len(word)
    guessed_letters = []
    guessed_words = []
    tries = 6
    guessed = False
    print("Let's play hangman!")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:
        guess = input("Please guess a letter or word:").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You've already guessed letter, please try again:", guess)
            elif guess not in word:
                print(guess, "is not in the word!")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Good job!", guess, "is in the word")
                guessed_letters.append(guess)
                word_completion = update_word_completion(word, word_completion, guess)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) > 1 and guess.isalpha():
            if guess in guessed_words:
                print("You've already guessed this word,", guess)
            elif guess != word:
                print(guess, "is not equal to the word!")
                tries -= 1
                guessed_words.append(guess)
            else:
                print("Congrats, you have guessed the word, you won!")
                print(word)
                guessed = True
        else:
            print("The input is in wrong format, please try again!")
        print(word_completion)  # Here we print word_completion in its updated form.
        print(display_hangman(tries))
        print("You have", str(tries), "tries left!")
        print("Your previous guessed letters are:", guessed_letters)
        print("Your previous guessed words are:", guessed_words)
        if tries == 0:
            print("Unfortunately, you've lost the game :(, The word was:", word)

def update_word_completion(word, word_completion, guess):
    new_completion = ""
    for i in range(len(word)):
        if word[i] == guess:
            new_completion += guess
        else:
            new_completion += word_completion[i]
    return new_completion

def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        """,
        # head, torso, both arms, and one leg
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
           -
        """,
        # head, torso, and both arms
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
           -
        """,
        # head, torso, and one arm
        """
           --------
           |      |
           |      O
           |     \\|
           |      |
           |     
           -
        """,
        # head and torso
        """
           --------
           |      |
           |      O
           |      |
           |      |
           |     
           -
        """,
        # head
        """
           --------
           |      |
           |      O
           |    
           |      
           |     
           -
        """,
        # initial empty state
        """
           --------
           |      |
           |      
           |    
           |      
           |     
           -
        """
    ]
    return stages[tries]

def main():
    word = get_word()
    play(word)

main()
