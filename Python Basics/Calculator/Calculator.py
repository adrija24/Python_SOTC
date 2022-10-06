#Calculator SOTC

num1 = int(input("Enter the 1st Number: "))
num2 = int(input("Enter the 2nd Number: "))
sign = input("Enter the operation [+, -, *, /]: ")

if sign == "+":
    print("Addition Result: ", num1 + num2)
elif sign == "-":
    print("Subtracton Result: ", num1 - num2)
elif sign == "*":
    print("Multiplication Result: ", num1 * num2)
elif sign == "/":
    print("Division Result: ", num1 / num2)
else:
    print("It's an Invalid Operator")
