first = input("Enter first number you want")
operator = input("Enter operator you want(+,-,/,*)")
second = input("Enter second number you want")

first = int(first)
second = int(second)

if operator == "+":
    print(first + second)
elif operator == "-":
    print(first - second)
elif operator == "*":
    print(first * second)
elif operator == "/":
    print(first / second)
else:
    print("you had enter invalid operator")
