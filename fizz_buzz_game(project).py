def fizz_buzz(number: int) -> str:
    """
    Get the number from the user and display the correct result i.e. fizz, buzz, fizz-buzz or number.

    :param number: Any int
    """

    if number in range(15,1000,15):
        result = "fizz buzz"
    elif number in range(5, 1000,5):
        result = "buzz"
    elif number in range(3,1000,3):
        result = "fizz"

    else:
        result = str(number)

    return  result

# so we have to write a programme in which human  and computer play a game called Fizz Buzz.
# i won't be writing about the game but rather the programme that enables us to play the game so we have got a function
# now first we have to start a loop which terminates when we reach 100 or if the player enters a wrong value.

print("""This is the Fizz Buzz game between you and coumputer.
I assume that you know the rules of the fizz buzz game and we are good to go. (and if you in a rare case don't then please refer the internet.)
So Now let me tell you the rules:
1. You have to enter the letter in small case ONLY
2. If your input is a number then only enter the number nothing else
3. You win the game if you clear the level you have chosen
4. Yes, you can choose the level according to the level of your brain. :) 
5. Currently there is no option to play next level when you complete a level.
Side Note: We will be shortly adding a lot of options in the game like sounds and animation stuff, as this beta version 
is just for testing of the code of the game kindly have patience and stay tuned for the next iteration of the game. 
Till then Best of Luck to bang your damn Brain with our Best game yet.
""")
input("Press enter to proceed. ")
print()

level = input("Please select the level you want to play 1, 2, 3, 4, 5 : ")
print()
levels = [10, 20, 30, 40, 50]
game_val = []
for values in range(1,100):
    game_val.append(fizz_buzz(values))
input("Please press enter to begin.")
print()
print()
print("Let's begin.")
print()
upper_limit = levels[int(level) - 1]
entry = "2"
turn = 1
while True:
    if turn == upper_limit or turn > upper_limit:
        print("Congrats! You have beaten the game.")
        break
    print("Computer: {}".format(game_val[turn - 1]))
    entry = input("\tEnter your value: ")
    if entry == game_val[turn]:
        print("Player: {}".format(entry))
    else:
        print("You Loose! You entered a wrong value")
        break
    turn = 2 + turn