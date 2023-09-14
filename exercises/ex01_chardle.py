"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730597416"

word = input("Enter a 5-character word: ")
if len(word) != 5:
    print("Error: Word must contain 5 characters.")
    exit()
char = input("Enter a single character: ")
if len(char) != 1:
    print("Error: Character must be a single character.")
    exit()

print("Searching for " + char + " in " + word)

instances = 0

if word[0] == char:
    print(char + " found at index 0")
    instances += 1 
if word[1] == char:
    print(char + " found at index 1")
    instances += 1
if word[2] == char:
    print(char + " found at index 2")
    instances += 1
if word[3] == char:
    print(char + " found at index 3")
    instances += 1
if word[4] == char:
    print(char + " found at index 4")
    instances += 1
if instances == 1:
    print(str(instances) + " instance of " + char + " found in " + word) 
elif instances > 1:
    print(str(instances) + " instances of " + char + " found in " + word)
else:
    print("No instances of " + char + " found in " + word)