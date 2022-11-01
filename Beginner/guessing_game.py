from random import randint


def check_guess(num, guess):
    if num == guess:
        print("You won!")
        return True
    elif num > guess:
        print("Too low!")
        return False
    print("Too high!")
    return False


if __name__ == "__main__":
    r_num = randint(0, 100)
    game_won = False

    guess = input("Make a guess:\n")

    while game_won != True:
        game_won = check_guess(r_num, int(guess))
        guess = input("Try again:\n")
