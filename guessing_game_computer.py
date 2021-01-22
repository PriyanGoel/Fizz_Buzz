low = 1
high = 1000
print("""Let's play a game!
So, in this game you have to think of a number between {} and {} and I will try to guess your number taking least amount of chances.""".format(low, high))
print("So, now please think of a number between {} and {}".format(low, high))
input("Press enter when you are ready to start the game. ")

guesses = 1
while low != high:
    guess = low + (high - low) // 2
    high_low = input(
        "My guess is {}. If the number you guessed is higher type h, if it's lower type l, and if my guess is correct then type c: ".format(
            guess)).casefold()
    if high_low =="h":
        low = guess + 1

    elif high_low == "l":
        high = guess - 1

    elif high_low == "c":
        print("I got it in {} guesses.".format(guesses))
        break
    else:
        print("Please enter h, l, c .")
    guesses = guesses + 1

else:
    print("Your number was {}".format(low))
    print("I got it in {} guesses.".format(guesses))