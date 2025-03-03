print("Welcome to Treasure Island. \n Your mission is to find the treasure.\n")
stage1 = input("Where do you want to go ? Left or Right\n")
if stage1 == "right" :
    print("You Fell into a hole.\n Game over ! :(\n")
elif stage1 == "left" :
    stage2 = input("Whether you want to swim or wait?\n ")
    if stage2 == "swim" :
        print("You were attacked by a trout.\n Game over! :( \n")
    elif stage2 == "wait" :
        stage3 = input("Through which door do you want to go? red , yellow , blue?\n")
        if stage3 == "red":
            print("Burned by fire.\n Game Over! :(\n")
        elif stage3 == "yellow" :
            print("You win!\n")
        elif stage3 == "Blue" :
            print("Eaten by beasts.\n Game Over! :( \n")
