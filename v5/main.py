import random

number = random.randint(1, 10)

for i in range(3):
    guess = int(input("Вгадайте число від 1 до 10: "))

    if guess == number:
        print("Ви вгадали!")
        break
    elif guess > number:
        print("Менше")
    else:
        print("Більше")

print("Загадане число було:", number)