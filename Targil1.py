

def calc(input):
    arg = input[1]
    num1= int(input[0])
    num2 = int(input[2])
    if arg == "+":
        return num1+num2
    elif arg == "-":
        return num1-num2
    elif arg == "*":
        return num1 * num2
    elif arg == "/":
        return num1 / num2


data = input(" Calc Me :")
calc(data)