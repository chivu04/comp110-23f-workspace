my_number_string: str = input("Guess a number: ")
my_number: int = int(my_number_string)

if my_number == 10:
    print("Right")
else:
    print("Wrong")