# Be sure to import random


def pick_number():
    """
    Returns a random number between 1 and 100
    """
    # Write code here
    pass


def guess(number):
    while True:
        your_number = int(input("Guess: "))
        # Write code here
        # "You got it!" if correct
        # "Lower" if too high
        # "Higher if too low


def play_game():
    print("Welcome! I picked a number between 1 and 100. Can you guess it?")
    number = pick_number()
    guess(number)


if __name__ == '__main__':
    play_game()
