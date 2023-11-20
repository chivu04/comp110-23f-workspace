"""EX03 - Structured Wordle."""

__author__ = "730597416"


def contains_char(word: str, char: str) -> bool:
    """Check if the character is present in the word."""  
    assert len(char) == 1
    
    index = 0

    while index < len(word):
        if word[index] == char:
            return True
        index += 1
    return False


WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def emojified(guess: str, secret: str) -> str:
    """Create an emojified representation of the guess compared to the secret."""
    assert len(guess) == len(secret)

    emojified_result = ""
    index = 0

    while index < len(guess):
        if guess[index] == secret[index]:
            emojified_result += GREEN_BOX
        elif contains_char(secret, guess[index]):
            emojified_result += YELLOW_BOX
        else:
            emojified_result += WHITE_BOX
        index += 1
    return emojified_result


def input_guess(expected_length: int) -> str:
    """Prompt the user for a guess and continue prompting until they provide a guess of the expected length."""
    user_guess = input(f"Enter a { expected_length} character word: ")
    new_guess = " "
    while len(user_guess) != expected_length:
        new_guess = input(f"That wasn't { expected_length} chars! Try again: ")
        user_guess = new_guess
    return user_guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret_word = "codes"

    turns = 0
    max_turns = 6
    won = False

    while turns < max_turns and not won:
        turns += 1
        print(f"\n=== Turn {turns}/{max_turns} ===")

        user_guess = input_guess(len(secret_word))

        codified_result = emojified(user_guess, secret_word)
        print(codified_result)

        if user_guess == secret_word:
            won = True

    if won:
        print(f"You won in {turns}/{max_turns} turns!")
    else:
        print(f"X/{max_turns} - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()