a = float(input("Введіть число a: "))
b = float(input("Введіть число b: "))
operation = input("Введіть дію (+, -, *, /): ")

if operation == "+":
    print("Результат:", a + b)

elif operation == "-":
    print("Результат:", a - b)

elif operation == "*":
    print("Результат:", a * b)

elif operation == "/":
    if b == 0:
        print("Ділення на нуль")
    else:
        print("Результат:", a / b)