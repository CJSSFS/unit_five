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
        guess_total = guess_total + 1
        






main()