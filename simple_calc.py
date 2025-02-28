operator = input("Enter an operator (+,-,*,/): ")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if operator == "+":
    result = round(num1 + num2)
    print(f"Your output is {result}")
elif operator == "-":
    result = round(num1 - num2)
    print(f"Your output is {result}")
elif operator == "*":
    result = round(num1*num2)
    print(f"Your output is {result}")
elif operator == "/":
    result = round(num1 / num2)
    print(f"Your output is {result}")
else:
    print("The operator is not valid")
    exit()