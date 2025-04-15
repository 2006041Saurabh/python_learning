from menu import MENU

resources = {
    "water" : 300,
    "coffee" : 100,
    "milk" : 300
}
money = 0.00

def make_coffee(coffee):
    water_needed = MENU[coffee]["ingredients"]["water"]
    coffee_needed = MENU[coffee]["ingredients"]["coffee"]
    milk_needed = MENU[coffee]["ingredients"]["milk"]

    water_left = resources["water"]
    coffee_left = resources["coffee"]
    milk_left = resources["milk"]
    print(f"Enjoy your {coffee} <3 \n")
    water_final = water_left - water_needed
    coffee_final = coffee_left - coffee_needed
    milk_final = milk_left - milk_needed

    resources["water"] = water_final
    resources["coffee"] = coffee_final
    resources["milk"] = milk_final

    print(
        f"Ingredients left are  water: {resources["water"]} , coffee : {resources["coffee"]} , milk : {resources["milk"]}")



machine_satus = True

while machine_satus == True:
    coffee_type = input("what would you like to have ('espresso', 'latte' , 'cappuccino' ) ?\n").lower()
    print("Enter the coins \n")
    quater = float(input("quater: "))
    dimes = float(input("dimes: "))
    nickles = float(input("nickles: "))
    pennies = float(input("pennies: "))
    total = quater * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
    total = round(total, 2)

    if total < MENU[coffee_type]["cost"]:
        print("The money is not sufficient , Money Refunded\n")
    else:
        water_needed = MENU[coffee_type]["ingredients"]["water"]
        coffee_needed = MENU[coffee_type]["ingredients"]["coffee"]
        milk_needed = MENU[coffee_type]["ingredients"]["milk"]

        water_left = resources["water"]
        coffee_left = resources["coffee"]
        milk_left = resources["milk"]

        if water_left < water_needed or coffee_left < coffee_needed or milk_left < milk_needed:
            print("Sorry the resources is not enough :(\n")
        else:
            make_coffee(coffee_type)
            money += MENU[coffee_type]["cost"]
            refund = total - MENU[coffee_type]["cost"]
            refund = round(refund,2)
            print(f"Money refunded: {refund}")
            print(f"Total money in machine: ${money} \n")


        off = input("enter 'off' to switch of the machine or enter 'on' ").lower()
        if off == "off":
            machine_satus = False
