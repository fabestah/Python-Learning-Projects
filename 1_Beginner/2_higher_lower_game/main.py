from random import choice
import game_data


def choose_accounts(data):
    """Chooses 2 accounts from the game_data file and checks for a one time duplicate"""
    a = choice(data)
    b = choice(data)
    if a == b:
        b = choice(data)
    return a, b


def choose_answer(a, b):
    """Evaluates the right answer based on the follower count"""
    if a["follower_count"] > b["follower_count"]:
        return a
    return b


def convert_pick(pick, a, b):
    """Converts the pick from the player into the dictionary he picked"""
    if pick == "a":
        return a
    return b


def check_win(pick, answer):
    """Checks if player picked the right account"""
    if pick is answer:
        return True
    return False


if __name__ == "__main__":
    game_win = True
    score = 0

    print(
        "Welcome to the Highler|Lower Game!\nYou have to pick the Instagram account which has more followers.\n\n"
    )
    while game_win == True:
        a, b = choose_accounts(game_data.data)
        answer = choose_answer(a, b)

        print(
            f"Compare A: {a['name']}, a {a['description']}, from {a['country']}\n\nVS.\n\n{b['name']}, a {b['description']}, from {b['country']}\n"
        )
        pick = input(f"Who has more followers?\nType 'A' or 'B': ").lower()

        pick = convert_pick(pick, a, b)
        game_win = check_win(pick, answer)
        if game_win:
            score += 1
            print(f"\nYou guessed it right, yay! Current score: {score}\nNext round:\n")
        else:
            print(f"\nYou lost! Score: {score}")
