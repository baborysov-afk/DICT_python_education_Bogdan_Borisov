import sys

# Начальное состояние кофемашины (согласно условию Этапа 4)
water = 400
milk = 540
coffee_beans = 120
disposable_cups = 9
money = 550


def print_state():
    """Функция вывода текущего состояния кофемашины"""
    print("\nThe coffee machine has:")
    print(f"{water} of water")
    print(f"{milk} of milk")
    print(f"{coffee_beans} of coffee beans")
    print(f"{disposable_cups} of disposable cups")
    print(f"${money} of money\n")  # Измените на грн, если требуется по условию


def check_resources(req_water, req_milk, req_beans):
    """Функция проверки, хватает ли ингредиентов для выбранного кофе"""
    if water < req_water:
        print("Sorry, not enough water!")
        return False
    if milk < req_milk:
        print("Sorry, not enough milk!")
        return False
    if coffee_beans < req_beans:
        print("Sorry, not enough coffee beans!")
        return False
    if disposable_cups < 1:
        print("Sorry, not enough disposable cups!")
        return False
    print("I have enough resources, making you a coffee!")
    return True


def buy_coffee():
    """Функция покупки кофе"""
    global water, milk, coffee_beans, disposable_cups, money

    choice = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n> ")

    if choice == "back":
        return

    # 1 - espresso: 250ml water, 0ml milk, 16g beans, cost 4
    if choice == "1":
        if check_resources(250, 0, 16):
            water -= 250
            coffee_beans -= 16
            disposable_cups -= 1
            money += 4

    # 2 - latte: 350ml water, 75ml milk, 20g beans, cost 7
    elif choice == "2":
        if check_resources(350, 75, 20):
            water -= 350
            milk -= 75
            coffee_beans -= 20
            disposable_cups -= 1
            money += 7

    # 3 - cappuccino: 200ml water, 100ml milk, 12g beans, cost 6
    elif choice == "3":
        if check_resources(200, 100, 12):
            water -= 200
            milk -= 100
            coffee_beans -= 12
            disposable_cups -= 1
            money += 6


def fill_machine():
    """Функция пополнения запасов машины"""
    global water, milk, coffee_beans, disposable_cups

    try:
        add_water = int(input("Write how many ml of water you want to add:\n> "))
        add_milk = int(input("Write how many ml of milk you want to add:\n> "))
        add_beans = int(input("Write how many grams of coffee beans you want to add:\n> "))
        add_cups = int(input("Write how many disposable coffee cups you want to add:\n> "))

        water += add_water
        milk += add_milk
        coffee_beans += add_beans
        disposable_cups += add_cups
    except ValueError:
        print("Please enter valid numbers.")


def take_money():
    """Функция извлечения денег из кассы"""
    global money
    print(f"I gave you {money}")
    money = 0


def main():
    """Главный цикл работы кофемашины"""
    while True:
        action = input("Write action (buy, fill, take, remaining, exit):\n> ").strip().lower()

        if action == "buy":
            buy_coffee()
        elif action == "fill":
            fill_machine()
        elif action == "take":
            take_money()
        elif action == "remaining":
            print_state()
        elif action == "exit":
            break
        else:
            print("Unknown action. Please choose buy, fill, take, remaining, or exit.")


if __name__ == "__main__":
    main()
