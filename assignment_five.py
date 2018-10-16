import random


def play():
    play = input("Would you like to play a game?")
    if play == "yes" or play == "y":
        return True
    else:
        return False


def draw():
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
                break
            print("Okay bye.")


main()