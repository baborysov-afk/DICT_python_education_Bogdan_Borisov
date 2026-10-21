import random


def main():
    try:
        num_friends = int(
            input("Enter the number of friends joining (including you):\n")
        )
    except ValueError:
        print("No one is joining for the party")
        return

    if num_friends <= 0:
        print("No one is joining for the party")
        return

    print("Enter the name of every friend (including you), each on a new line:")
    friends = {}
    for _ in range(num_friends):
        name = input()
        friends[name] = 0

    try:
        total_amount = float(input("Enter the total amount:\n"))
    except ValueError:
        return

    lucky_choice = input(
        'Do you want to use the "Who is lucky?" feature? Write Yes/No:\n'
    )

    lucky_one = None
    # Щасливчика можна обирати, тільки якщо людей більше ніж 1
    if lucky_choice == "Yes" and num_friends > 1:
        lucky_one = random.choice(list(friends.keys()))
        print(f"{lucky_one} is the lucky one!")
    else:
        print("No one is going to be lucky")

    # Перерахунок суми
    if lucky_one:
        split_amount = round(total_amount / (num_friends - 1), 2)
        for friend in friends:
            if friend == lucky_one:
                friends[friend] = 0
            else:
                friends[friend] = split_amount
    else:
        split_amount = round(total_amount / num_friends, 2)
        for friend in friends:
            friends[friend] = split_amount

    print(friends)


if __name__ == "__main__":
    main()
