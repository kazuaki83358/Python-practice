print("Enter first number")
num1 = input()
print("Enter second number")
num2 = input()
print("Enter the operation")
operation = input()
if operation == "+":
    print(int(num1) + int(num2))
elif operation == "-":
    print(int(num1) - int(num2))
elif operation == "*":
    print(int(num1) * int(num2))
elif operation == "/":
    print(int(num1) / int(num2))
else:
    print("Invalid operation")
