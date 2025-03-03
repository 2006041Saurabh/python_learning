print("Welcome to the pizza delivery System\n")
size = input("What size pizza do you want ? S , M or L : \n")
pepperoni  = input("Do you want pepporoni on your pizza ? Y or N:")
extra_cheese = input("Do you want extra chsesse ? Y or N :")

bill = 0

if( size == "S") :
    bill += 15
    if(pepperoni == "Y") :
        bill += 2
    if(extra_cheese == "Y") :
        bill += 1
elif (size == "M"):
    bill += 20
    if (pepperoni == "Y"):
        bill += 3
    if (extra_cheese == "Y"):
        bill += 1
elif (size == "L") :
    bill += 25
    if (pepperoni == "Y"):
        bill += 3
    if (extra_cheese == "Y"):
        bill += 1

print(f"Your final bill is: ${bill}\n")
