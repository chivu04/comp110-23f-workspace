"""EX02 - One-Shot Wordle - Loops!"""

__author__ = "730597416"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

index: int = 0
emoji: str = ""

secret_word: str = "python"
guess: str = input(f"What is your {len(secret_word)}-letter guess? ")

while len(guess) != len(secret_word):
    new_guess = input(f"That was not {len(secret_word)}-letters! Try again: ")
    guess = new_guess

while index < len(secret_word):
    if guess[index] == secret_word[index]:
        emoji += GREEN_BOX
        index += 1
    else:
        exist: bool = False
        alternate: int = 0
        while exist is False and alternate < len(secret_word):
            if secret_word[alternate] == guess[index]:
                exist = True
            else:
                alternate += 1
        if exist is True:
            emoji += YELLOW_BOX
        else:
            emoji += WHITE_BOX
    
        index += 1

print(emoji)
if guess != secret_word:
    print("Not quite. Play again soon!")
else:
    print("Woo! You got it!")