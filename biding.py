
dic = {}

should_continue = True

while should_continue == True:
    name = input("Enter your name\n")
    bid = int(input("Enter your bid\n"))
    dic[name] = bid

    more = input("Are there more persons\n").lower()

    if more == "yes":
        print("\n" * 100)
        should_continue = True
    else:
        should_continue = False

highest_bid = 0
winner = ""

for user in dic:
    b = dic[user]
    if b > highest_bid:
        highest_bid = b
        winner = user

print(f"The winner of the bid is {winner} with the bid of {highest_bid}\n")
