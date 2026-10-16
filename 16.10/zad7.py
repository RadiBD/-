
a = float(input("Въведи първото число: "))
b = float(input("Въведи второто число: "))

op = input("Въведи действие (+, -, *, /): ")

if op == "+":
    print("Резултат:", a + b)
elif op == "-":
    print("Резултат:", a - b)
elif op == "*":
    print("Резултат:", a * b)
elif op == "/":
    if b != 0:
        print("Резултат:", a / b)
    else:
        print("Деление на нула е невъзможно")
else:
    print("Невалидно действие")
