score = int(input("Введіть кількість балів: "))

if score <= 49:
    print("Незадовільно")
elif score <= 69:
    print("Задовільно")
elif score <= 89:
    print("Добре")
else:
    print("Відмінно")