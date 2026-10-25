


def read_file(filename):
    file = open(filename, "r")
    content = file.read()
    return content

def alarm_count(file_content):
    count = 0
    for line in file_content.split("\n"):
        num = int(line.split(" : ")[0])
        count +=num

    print(f"Total Alarms : {count}")

def show_5(file_content):
    list_of_cities = []
    for line in file_content.split("\n"):
        list_of_cities.append(line)
    five= list_of_cities[:5]
    list_names = []
    for city in five:
        list_names.append(city.split(" : ")[1])
    print(sorted(list_names))



file_content = read_file("Alarms.txt")
alarm_count(file_content)
show_5(file_content)