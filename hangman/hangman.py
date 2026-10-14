import random

print("HANGMAN")
words = ['python', 'java', 'javascript', 'php']
secret_word = random.choice(words)
hidden_word = list("-" * len(secret_word))

attempts = 8
guessed_letters = set()  # Множина для збереження ВСІХ раніше введених літер

while attempts > 0:
    print()
    print("".join(hidden_word))

    # Перевірка на перемогу
    if "-" not in hidden_word:
        print("You guessed the word!")
        print("You survived!")
        break

    letter = input("Input a letter: ")

    # 1. Перевірка: чи введено рівно один символ
    if len(letter) != 1:
        print("You should input a single letter")
        continue

    # 2. Перевірка: чи є символ малою англійською літерою
    if not (letter.islower() and letter.isalpha()):
        print("Please enter a lowercase English letter")
        continue

    # 3. Перевірка: чи вводили цю літеру раніше
    if letter in guessed_letters:
        print("You've already guessed this letter")
        continue

    # Додаємо літеру до списку використаних
    guessed_letters.add(letter)

    # 4. Перевірка наявності літери у загаданому слові
    if letter in secret_word:
        for i in range(len(secret_word)):
            if secret_word[i] == letter:
                hidden_word[i] = letter
    else:
        print("That letter doesn't appear in the word")
        attempts -= 1
else:
    print("You lost!")



