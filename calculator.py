operator =input("Choose an operator(+ - * /): ")
num1 = float(input("Enter a Number: "))
num2 = float(input("Enter a number: "))

if operator == "+":
    result = num1 + num2
    print(round(result))
elif operator == "-":
    result = num1 - num2 
    print(round(result))
elif operator == "*":
    result = num1 * num2
    print(round(result))
elif operator == "/":
    result = num1 / num2
    print(round(result))
else:
    print(f"{operator} it is not a valid operator") 