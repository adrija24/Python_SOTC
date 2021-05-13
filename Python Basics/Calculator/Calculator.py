#Calculator SOTC

num_1 = int(input("Enter the 1st Number: "))
num_2 = int(input("Enter the 2nd Number: "))
sign = input("Enter the operation [+, -, *, /]: ")

if sign == "+":
    print("Addition Result: ", num_1 + num_2)
elif sign == "-":
    print("Subtracton Result: ", num_1 - num_2)
elif sign == "*":
    print("Multiplication Result: ", num_1 * num_2)
elif sign == "/":
    print("Division Result: ", num_1 / num_2)
else:
    print("It's an Invalid Operator")