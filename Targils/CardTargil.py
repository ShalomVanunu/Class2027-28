
numbers = []

for num1 in range(10):
    for num2 in range(10):
        for num3 in range(10):
            numbers.append(str(num1)+str(num2)+str(num3))

print(numbers)