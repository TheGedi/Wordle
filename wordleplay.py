from colorama import Fore
from letter_state import LetterState
from wordle import Wordle
import random

def main():
    word_set = load_word("valid_words.txt")
    secret = random.choice(list(word_set) )
    wordle = Wordle(secret)
    while wordle.attemptable:
        guess = input("\nEnter your guess: ").upper()
        if len(guess) != wordle.MAX_LENGTH:
            print(Fore.RED + "Invalid Input given!" + Fore.RESET)
            continue
        if guess not in word_set:
            print(Fore.RED + "Invalid Input given!" + Fore.RESET)
            continue

        wordle.attempt(guess)
        display(wordle)
    if wordle.solved:
        print("\nYou guessed the word! ")
        play_again()
    else:
        print("\nYou have failed to guess the word.")
        print(f"The secret word was: {wordle.secrect}")
        play_again()
    
    




def display(wordle: Wordle):
    print(f"You have {wordle.guesses_remaining} attempts remaining\n")
    for i in wordle.attempts:
        result = wordle.guess(i)
        coloured_result = colored(result)
        print(coloured_result)
    for _ in range(wordle.guesses_remaining):
        print(" ".join(["-"] * wordle.MAX_LENGTH ))

def colored(result: list[LetterState]):
    colored_result = []
    for letter in result:
        if letter.in_position:
            colour = Fore.GREEN
        elif letter.in_word:
            colour = Fore.YELLOW
        else:
            colour = Fore.WHITE
        coloured_letter = colour + letter.Character + Fore.RESET
        colored_result.append(coloured_letter)
    return " ".join(colored_result)

def load_word(path: str):
    word_set = set()
    with open(path, "r") as f:
        for line in f.readlines():
            word = line.strip().upper()
            word_set.add(word)
    return  word_set

def play_again():
        play_on = input("\nDo you wish to continue? ").upper()
        match play_on:
            case 'YES':
                main()
            case 'NO':
                print("\nThanks for playing!")



if __name__ == "__main__":
    main()