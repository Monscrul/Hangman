import random
from temp3 import states


def word_shower():
    flag = True
    while flag:
        rand_word_list = ["boys", "man", "farting"]
        secret_word = random.choice(rand_word_list)

        displayed_word = "_" * len(secret_word)

        right_guesses = set()
        wrong_guesses = set()
        displayed_word = "_" * len(secret_word)
        displayed_state_index = 6

        while flag:
            displayed_state = states[displayed_state_index]
            print(displayed_state)
            print(displayed_word)
            print(f"Lives: {displayed_state_index}")
            guessed_letter = str(input("Guess a letter: "))

            if guessed_letter in secret_word:
                right_guesses.add(guessed_letter)
                for i in range(len(secret_word)):
                    if secret_word[i] == guessed_letter:
                        displayed_word = displayed_word[:i] + guessed_letter + displayed_word[i+1:]
            else:
                wrong_guesses.add(guessed_letter)
                displayed_state_index -= 1
                print("Try again!")

            if "_" not in displayed_word:
                print("Congrats you won! the word was " + secret_word)
                flag = False
                break
            elif len(wrong_guesses) == 6:
                print(states[0])
                print("You lost, no lives left")
                flag = False
                break


word_shower()

