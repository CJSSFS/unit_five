# Chad Scott
# Date: 10/17/18
# Last modified 10/17/18
# In this program the user is playing a guessing game to try and guess what random number is chosen


import random


def play():
    """
    This Function asks the user if they would like to play a game
    :return: True if the user says yes
             False if the user says they do not want to play
    """
    play1 = input("Would you like to play a game?")
    if play1 == "yes" or play1 == "y":
        return True
    else:
        return False


def draw():
    """
    This function draws a random number for the user to guess
    :return: This returns a random integer for the user to guess
    """
    return random.randint(1, 100)


def main():
    while True:
        if play():
            guess_total = 0
            number = draw()
            while True:
                guess = int(input("Guess my number:"))
                guess_total = guess_total + 1
                if number == guess:
                    print("You guessed it")
                    break
                elif guess < number:
                    print("Your number was too low")
                elif guess > number:
                    print("Your number was too high")
            print("You guessed it in", guess_total, "tries")
        else:
            break
    print("Okay bye")


main()