
while True :
    text = input(" write :")
    if text == "bye":
        break
    file = open("data", "w")
    file.write(text+"\n")
