bot_name = "DICT_Bot"
birth_year = 2026

print(f"Hello! My name is {bot_name}.")
print(f"I was created in {birth_year}.")
print("Please, remind me your name.")
your_name = input("> ")
print(f"What a great name you have, {your_name}!")
print("Let me guess your age.")
print("Enter remainders of dividing your age by 3, 5 and 7.")

remainder3 = int(input("> "))
remainder5 = int(input("> "))
remainder7 = int(input("> "))

your_age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105
print(f"Your age is {your_age}; that's a good time to start programming!")
print("Now I will prove to you that I can count to any number you want.")
max_number = int(input("> "))

for i in range(max_number + 1):
    print(f"{i} !")

print("Completed, have a nice day!")
print("Let's test your programming knowledge.")
print("Why do we use methods?")
print("1. To repeat a statement multiple times.")
print("2. To decompose a program into several small subroutines.")
print("3. To determine the execution time of a program.")
print("4. To interrupt the execution of a program.")

correct_answer = 2

while True:
    user_answer = int(input("> "))
    if user_answer == correct_answer:
        break
    else:
        print("Please, try again.")

print("Completed, have a nice day!")
print("Congratulations, have a nice day!")
