print("Welcome to the tip calculator!")
bill = int(input("what was the total bill ?\n"))
rate = int(input("How much tip would you like to give? 10 , 12, or 15?\n"))
people = int(input("How many people to split the bill?\n"))

total = (bill + bill * (rate/100))/people
total = round(total,2)

print(f"Each person should pay: {total}\n")