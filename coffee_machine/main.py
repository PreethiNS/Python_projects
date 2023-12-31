MENU = {
    "espresso":{
        "ingredients":{
            "water":50,
            "coffee":18,
        },
        "cost":1.5
    },
    "latte":{
        "ingredients":{
            "water":200,
            "milk":150,
            "coffee":24,
        },
        "cost":2.5
    },
    "cappuccino":{
        "ingredients":{
            "water":250,
            "milk":100,
            "coffee":24,
        },
        "cost":3.0,
    }
}

profit = 0
resources = {
    "water":300,
    "milk":200,
    "coffee":100,
}

def is_resource_Sufficient(order_ingredients):
    """returns True when order can be made, False if ingredients are insufficient"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True

def process_coins():
    """returns the total calculated from coins inserted"""
    print("please insert coins.")
    total = int(input("how many quartes?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennis?: ")) * 0.01
    return total


def is_transaction_successful(money_recieved,drink_cost):
    """return True when the payment is accepted, or False if money is insufficient"""
    if money_recieved >= drink_cost:
        change = round(money_recieved - drink_cost,2)
        print(f"here is ${change} in change")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")


def make_coffee(drink_name,order_ingredients):
    """deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"here is your {drink_name} ")


is_on = True
#prompt the user
while is_on:
    choice=input("what would you like? (espresso/latte/cappuccino): ").lower()
#Turn off the coffee machine
    if(choice=="off"):
        is_on = False
    elif choice == "report":
        print(f"water:{resources['water']}")
        print(f"milk:{resources['milk']}")
        print(f"coffee:{resources['coffee']}")
        print(f"Money:${profit}")
    else:
        drink = MENU[choice]
        if is_resource_Sufficient(drink["ingredients"]):
            payment =process_coins()
            #check transaction successful
            if is_transaction_successful(payment,drink["cost"]):
                make_coffee(choice,drink["ingredients"])






