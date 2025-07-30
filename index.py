n1 = int(input("Enter a number: "))
n2 = int(input("Enter another number: "))

o = (input("Enter a mathematical operation (+, -, *, /): "))

if o == "+":
    result = n1 + n2
    print(f"{n1} + {n2} = {result}")
elif o == "-":
    result = n1 - n2
    print(f"{n1} - {n2} = {result}")
elif o == "*":
    result = n1 * n2
    print(f"{n1} * {n2} = {result}")
elif o == "/":
    if n2 != 0:
        result = n1 / n2
        print(f"{n1} / {n2} = {result}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation. Please enter +, -, *, or /.")