
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

profit = 0
resource = {
    'water' : 500,
    'milk':200,
    'coffee': 80
}



def is_resource(order_indredients):
    for item in order_indredients:
        if order_indredients[item] > resource[item]:
            print("Not enough resource.")
            return False
    return True

def process_coins():
    print("How many coins ?")
    total = int(input("How many Quartares ?")) * 0.25
    total += int(input("How many Dimes ?")) * 0.1
    total += int(input("How many Nickeles ?")) * 0.05
    total += int(input("How many Pennyes ?")) * 0.01
    return total

def is_transaction(money_recived, drink_cost):
    if money_recived >= drink_cost:
        change = round((money_recived - drink_cost), 2)
        print(f"The Change is {change}")
        global profit
        profit += drink_cost
        return True
    else:
        print("Not enough money.")
        return False


def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resource[item] -= order_ingredients[item]
    print(f"Here is your coffee {drink_name}☕.")

machine = True

while machine:

    user_input = input("Enter (espresso\latte\cappuccino) :").lower()
    if user_input == 'off':
        machine = False
    
    elif user_input == 'report':
        print(f"Water :{resource['water']}ml")
        print(f"Milk :{resource['milk']}ml")
        print(f"Coffee :{resource['coffee']}g")
        print(f"Money :{profit}/-")
    
    elif user_input in MENU :
        drink = MENU[user_input]

        if is_resource(drink['ingredients']) :
            payment = process_coins()
            if is_transaction (payment, drink["cost"]):
                make_coffee(user_input, drink["ingredients"])





# """1. menu\report
# menu = what would you like?

# check resource
# process coins
# transaction sucessful
# make coffeee with outputtttttt

# """