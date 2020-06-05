import random
from custom_words import shuffled_answers

def answerer():
    answer = shuffled_answers.popitem()
    word = answer[0].upper()
    player = answer[1]['player']
    theme = answer[1]['theme']
    hint = answer[1]['hint']
    return word, player, theme, hint

def play(word, player, theme, hint):
    guessed = False
    guessed_letters = []
    guessed_words = []
    word_completion = ""
    tries = 6
    counter = len(word.split())
    holder = word.split()
    while counter > 0:
        word_completion += "_" * len(holder[0]) + "\n"
        counter -= 1
        holder.pop(0)
    print("\nFamily Hangman Time!")
    print(display_hangman(tries))
    print(word_completion)
    print('\n')
    print(player)
    while not guessed and tries > 0:
        guess = input("Guess a letter or a word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print(f"You already guessed '{guess}', loser.")
            elif guess not in word:
                print(f"No! '{guess}' is NOT in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print(f"You got lucky...'{guess}' is in the word")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif guess == '?':
            tries -= 1
            print(hint)
        elif len(guess) > 1 and len(guess) != len(word):
            print(f"'{guess}' hasn't got the right amount of letters. I know, counting is hard...")
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print(f"You already guessed '{guess}', dummy")
            if guess != word:
                print(f"Ha! Nice try, '{guess}' is not the word. Maybe stick with letters, it's easier.")
            else:
                guessed = True
                word_completion = word
        else:
            print("\nNot a valid guess. That is so obviously not a valid guess. Please, this is serious.")
        print(display_hangman(tries))
        print(word_completion)
        print('\n')
    if guessed:
        print(f"{player}, you're a winner! The theme is {theme}.")
    else:
        print(f"No surprise {player} ran out of tries. The answer is {word}, and the theme is {theme}.")



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
                   |     /
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
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
    # try:
        answer, player, theme, hint = answerer()
        play(answer, player, theme, hint)
        while input("Play Again? (Y/N) ").upper() == "Y":
            answer, player, theme, hint = answerer()
            play(answer, player, theme, hint)
    # except:
    #     print("\n\nOh no, there are no more words!\n\n")

if __name__ == "__main__":
    main()
