import random
def guess(level):
    chance = 0
    if level == "easy":
        chance = 10
    elif level == "hard":
        chance = 5
    correct_num = random.choice(range(1, 101))

    while chance != 0:
        num = int(input("Guess the number\n"))
        if num == correct_num:
            print("Correct number , You won !\n")
            break
        elif num > correct_num:
            print("Too High!\n")
            chance -= 1
            print(f"Left chances: {chance}\n")
        elif num < correct_num:
            print("Too Low!")
            chance -= 1
            print(f"Left chances: {chance}\n")




stage = input("Enter the level you want to play , Hard or easy ?").lower()
guess(stage)
