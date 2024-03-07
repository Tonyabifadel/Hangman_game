import random

def display_hangman(chances):
    hangman_stages = [
        """
        ________
        |      |
        |      0
        |     /|\\
        |     / \\
        |
        """,
        """
        ________
        |      |
        |      0
        |     /|\\
        |     /
        |
        """,
         """
        ________
        |      |
        |      0
        |     /|\\
        |
        |
        """,
        """
        ________
        |      |
        |      0
        |     /|
        |
        |
        """,

        """
        ________
        |      |
        |      0
        |     /
        |
        |
        """,
         """
        ________
        |      |
        |      0
        |
        |
        |
        """,
        """
        ________
        |      |
        |
        |
        |
        |
        """



    ]



    print(hangman_stages[chances-1])



def get_random_word():
    word_list = ["apple", "banana", "orange", "grape", "melon", "strawberry", "kiwi", "peach", "pineapple"]
    return random.choice(word_list)

def initialize_guessed_word(word):
    return '_' * len(word)


def start_hangman_game():
    word_to_guess = get_random_word()
    guessed_word_placeholder = initialize_guessed_word(word_to_guess)
    remaining_chances = 5
    flag = False

    while True:
        if remaining_chances == 0:
            print("You Lost, the word was: " + word_to_guess)
            print("Better luck next time")
            break

        print("Guess the word ")
        print(guessed_word_placeholder, end='')
        print("\t(word contains " + str(len(word_to_guess)) + " letters)")
        print("You have " + str(remaining_chances) + " chances left ")

        user_input = input("Enter a character: ")
        if not user_input.isalpha() or len(user_input) != 1 :
            print("Please enter a single alphabet only")
            continue

        for index, char in enumerate(list(word_to_guess)):
            if char == user_input:
                temp_list = list(guessed_word_placeholder)
                temp_list[index] = char
                guessed_word_placeholder = ''.join(temp_list)
                flag = True

        if flag:
            flag = False
        else:
            remaining_chances -= 1

        if '_' not in guessed_word_placeholder:
            print("\nYou Won! The word was: " + word_to_guess)
            print("You got it in " + str(5 - remaining_chances) + " guess")
            break
        else:
            display_hangman(remaining_chances)
        print()

print("===== Welcome to the Hangman Game =====")
while True:
    user_choice = input("Do you want to play hangman? (yes/no): ")
    if 'yes' in user_choice.lower():
        start_hangman_game()
    elif 'no' in user_choice.lower():
        print('Goodbye')
        break
    else:
        print("Enter a valid choice.")
    print("\n")
