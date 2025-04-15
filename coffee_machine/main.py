from menu import MENU

resources = {
    "water" : 300,
    "coffee" : 100,
    "milk" : 100
}

def make_coffee(coffee):
    water_needed = MENU[coffee]["ingredients"]["water"]
    coffee_needed = MENU[coffee]["ingredients"]["coffee"]
    milk_needed = MENU[coffee]["ingredients"]["milk"]

    water_left = resources["water"]
    coffee_left = resources["coffee"]
    milk_left = resources["milk"]

    if water_left < water_needed or coffee_left < coffee_needed or milk_left < milk_needed:
        print("Sorry the resources is not enough :(\n")
    else:
        print(f"Enjoy your {coffee} <3 \n")


coffee_type = input("what would you like to have ('espresso', 'latte' , 'cappuccino' ) ?").lower()

make_coffee(coffee_type)
