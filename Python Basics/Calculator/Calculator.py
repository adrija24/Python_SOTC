#Calculator SOTC

num = int(input("Enter the 1st Number: "))
num_1 = int(input("Enter the 2nd Number: "))
sign = input("Enter the operation [+, -, *, /]: ")

if sign == "+":
    print("Addition Result: ", num + num_1)
elif sign == "-":
    print("Subtracton Result: ", num - num_1)
elif sign == "*":
    print("Multiplication Result: ", num * num_1)
elif sign == "/":
    print("Division Result: ", num / num_1)
else:
    print("It's an Invalid Operator")
