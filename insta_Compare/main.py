from data import data
import random

def format_data(account):
    """Format the account data into printable format"""
    account_name = account["name"]
    account_desc = account["description"]
    return f"{account_name}, a {account_desc}"


def check_answer(user_guess, a_followers , b_followers):
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"

score = 0

game_should_continue = True

while game_should_continue:
    celeb1 = random.choice(data)
    celeb2 = random.choice(data)

    if celeb1 == celeb2:
        celeb2 = random.choice(data)

    print(f"Comapre A: {format_data(celeb1)}")
    print("vs\n")
    print(f"Against B: {format_data(celeb2)}.")

    # Ask user for a guess

    guess = input("Who has more followerrs? Type 'A' or 'B':").lower()

    # check if the user is correct

    a_follower_count = celeb1["followers"]
    b_follower_count = celeb2["followers"]

    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    if is_correct:
        score += 1
        print(f"You are right! , Your score is: {score}")
    else:
        print(f"Sorry, that's wrong . Final score: {score}")
        game_should_continue = False



