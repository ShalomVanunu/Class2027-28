
file = open("text.txt","r")  #  r - read ,w- write, a- append
file_content_lines = file.readlines()
file.close()
file = open("text.txt","r")  #  r - read ,w- write, a- append
file_content = file.read()


print(file_content)
print(file_content_lines)

with open("text.txt","r") as file:
    print(file.read())
    print(file.readlines())