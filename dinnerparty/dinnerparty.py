import random

print("Enter the number of friends joining (including you):")
num_of_friends = int(input("> "))

if num_of_friends <= 0:
    print("No one is joining for the party")
else:
    friends_dict = {}
    print("Enter the name of every friend (including you), each on a new line:")
    for _ in range(num_of_friends):
        name = input("> ")
        friends_dict[name] = 0

    print("Enter the total amount:")
    total_amount = float(input("> "))

    print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
    lucky_choice = input("> ")

    if lucky_choice == "Yes":
        lucky_one = random.choice(list(friends_dict.keys()))
        print(f"{lucky_one} is the lucky one!")

        # Перераховуємо суму на (n - 1) людей
        new_split_value = round(total_amount / (num_of_friends - 1), 2)

        for name in friends_dict:
            if name == lucky_one:
                friends_dict[name] = 0
            else:
                friends_dict[name] = new_split_value
    else:
        print("No one is going to be lucky")
        # Стандартний поділ на всіх
        split_value = round(total_amount / num_of_friends, 2)
        for name in friends_dict:
            friends_dict[name] = split_value

    print(friends_dict)
