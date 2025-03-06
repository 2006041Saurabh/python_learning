import random
my_list = ["current" , "main","learning\n"]
random_word = random.choice(my_list)

print(random_word)

placeholder = ""
word_length = len(random_word)

for position in range(word_length):
    placeholder += "_"
print(placeholder)

correct_letters = []

game_over = False


while not game_over:
    guess = input("Enter a letter\n").lower()

    display = ""

    for letter in random_word:
        if letter == guess:
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)

    if "_" not in display:
        game_over = True
        print("You Win!")