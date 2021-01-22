import random


def get_integer(prompt):
    """
    Get an integer form Standard Input (stdin).
    The function keeps looping around itself utill a
    valid `int` is entered.

    :param prompt: The string that user will see, when they are prompted to
                enter a value.
    :return: The integer that the user enters.
    """
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)
        else:
            print("That was invalid entry, please enter again.")


print("This is a guessing game where computer will think of number and the user will have to make certain guesses to get to the number that computer thought of, ")
print("The point of the game is to reach the correct number by taking minimum number of guesses.")
print("You can use Mathematics to be more efficient.")
input("Press ENETER when you are ready to begin. ")


answer = random.randint(2, 998)
guess = get_integer("Please enter your number i.e. between 1 and 1000: ")
number_of_guess = 1


while guess != answer:
    number_of_guess += 1
    if guess > answer:
        print("Please guess lower.")
    else:
        print("Please guess higher.")
    guess = get_integer("That wasn't right, Please guess again (or you can submit 0 as an answer to quit the game): ")

    if guess == 0:
        print("Well better luck next time.")
        break
else:
    print("You took {} guesses to reach the answer.".format(number_of_guess))
    print("Well done.")