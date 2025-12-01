MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "Money": 0
}
coins={
    "quarters": 0.25,
    "dimes": 0.10,
    "nickles": 0.05,
    "pennies": 0.01
}

total_coins=0
status=True
def off():
    print("Switching off the Machine....")
    exit()
def report():
    res=resources
    for key, value in res.items():
        print(f"{key}: {value}")
    exit()

def check_resources(choice):
    for key1,value1 in MENU[choice]['ingredients'].items():
        if value1 > resources[key1]:
            print(f"Sorry there is not enough {key1} available to make the coffee!!!")
            exit()
    print("Please insert coins.")
#Program starts from here
while status:
    coffee_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if coffee_choice == "report":
        report()
    if coffee_choice == "off":
        off()
    check_resources(coffee_choice)
    quarters = int(input("how many quarters?:"))* coins['quarters']
    dimes = int(input("how many dimes?:"))* coins['dimes']
    nickles = int(input("how many nickles?:"))* coins['nickles']
    pennies = int(input("how many pennies?:"))* coins['pennies']
    total_coin = quarters + dimes + nickles + pennies

    if total_coin >= MENU[coffee_choice]["cost"]:
        print("Preparing your coffee. Please wait .....")
        change=total_coin - MENU[coffee_choice]["cost"]
        resources["Money"] += MENU[coffee_choice]["cost"]
        for i,j in MENU[coffee_choice]["ingredients"].items():
            resources[i] -= j
        if change == 0:
            print("Enjoy your coffee... ")
        else:
            print(f"Enjoy your coffee... Here is ${round(change, 2)} dollars in change.”")
    else:
        print(f"Sorry that's not enough money. Money refunded. ${total_coin}")
        status = False