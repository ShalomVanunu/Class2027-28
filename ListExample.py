text = "my name is shalom"

list_names = text.split(" ")
list_m = text.split("m")

print(list_names)

print(" ".join(list_names))

list_of_names= [ 'yuli', 'itai', 'yehonatan']

print(list_of_names)
print(list_of_names[0])
for name in list_of_names:
    print(name)