from data import MENU, resources

INGREDIENTS = [k for k in resources.keys()]
available_resources = [v for v in resources.values()]
cash = 0


def ingredients_needed(order: str) -> list[int]:
    """Create a list of ingredients ammount needed to prepare a drink."""
    consumption_list = [v for v in MENU[order]["ingredients"].values()]
    if len(consumption_list) < 3:  # espresso does not get milk
        consumption_list.insert(1, 0)
    return consumption_list


def enough_ingredients(i_have: list[int], i_need: list[int]):
    """Return a list [str] of 'under ammount' ingredient(s) needed to prepare an ordered drink. 
    Return None if all ingredient ammount are sufficient to prepare an ordered drink.
    """
    subtraction = map(lambda i1, i2: i1 - i2, i_have, i_need)
    availability_dict = dict(zip(INGREDIENTS, subtraction))
    return [k for k, v in availability_dict.items() if v < 0]


def sum_of_coins() -> float:
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))
    return round(quarters * 0.25 + dimes * 0.1 + nickels * 0.05 + pennies * 0.01, 2)


def operate():
    """Puts coffee machine in operation."""
    while True:
        order = input("What would you like? (espresso/latte/cappuccino): ")
        if order == "off":
            return "Machine is now off."
        elif order == "report":
            for ingredient, ammount in resources.items():
                if ingredient != "coffee":
                    print(f"{ingredient}: {ammount}ml")
                else:
                    print(f"{ingredient}: {ammount}g")
            global cash
            print(f"Money: ${cash}")
            continue
        ml_and_g = ingredients_needed(order)
        check_if = enough_ingredients(
            available_resources, ml_and_g)
        if len(check_if) > 0:
            for ingredient in check_if:
                print(f"Sorry, there is not not enough {ingredient}.")
            continue
        payment = sum_of_coins()
        cost = MENU[order]["cost"]
        if payment < cost:
            print("Sorry, that's not enought money. Money refunded.")
            continue
        elif payment > cost:
            print(f"Here is ${round(payment - cost, 2)} in change.")
        cash += cost
        available_resources[0] -= ml_and_g[0]
        available_resources[1] -= ml_and_g[1]
        available_resources[2] -= ml_and_g[2]
        print(f"Here is your {order}. Enjoy!")

